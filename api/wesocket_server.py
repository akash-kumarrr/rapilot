from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query
from schemas.driver import DriverLiveLoation as Driver
from schemas.ride import RideCreate as RideRequest

router = APIRouter(prefix="/ws", tags=["Ride Request Websocket"])


class WebsocketConnectionManager:
    def __init__(self):
        # 1. Properly initialized dictionary
        self.active_drivers: dict[WebSocket, Driver] = {}

    async def connect_driver(self, websocket: WebSocket, driver: Driver):
        await websocket.accept()
        # 2. Assign to active_drivers dictionary
        self.active_drivers[websocket] = driver

    def disconnect_driver(self, websocket: WebSocket):
        # 3. Safe remove without re-accepting
        self.active_drivers.pop(websocket, None)

    async def broadcast_ride_request(self, ride_request: RideRequest) -> int:
        notified_count = 0
        # Iterate safely over active driver sessions
        for ws, driver in list(self.active_drivers.items()):
            if getattr(driver, "live_geo_hash", None) == ride_request.starting_point_geohash:
                try:
                    # 4. Await send_json and pass dict via model_dump()
                    await ws.send_json({
                        "event": "NEW_RIDE_REQUEST",
                        "request": ride_request.model_dump()
                    })
                    notified_count += 1
                except Exception:
                    self.disconnect_driver(ws)
        return notified_count

    def update_location(self, websocket: WebSocket, live_long: float, live_lat: float, geo_hash: str = None):
        driver = self.active_drivers.get(websocket)
        if driver:
            driver.longitude = live_long
            driver.latitude = live_lat
            if geo_hash:
                driver.live_geo_hash = geo_hash


manager = WebsocketConnectionManager()


# 5. Accept primitives via Path & Query parameters for WebSocket handshake
@router.websocket("/driver/{driver_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    driver_id: int,
    initial_geohash: str = Query(...)
):
    # Construct the Driver schema instance internally
    driver = Driver(id=driver_id, live_geo_hash=initial_geohash)
    await manager.connect_driver(websocket, driver)

    try:
        while True:
            data = await websocket.receive_json()
            
            # Update live location state if coordinates/geohash sent in frame
            if "live_long" in data and "live_lat" in data:
                manager.update_location(
                    websocket, 
                    live_long=data["live_long"], 
                    live_lat=data["live_lat"],
                    geo_hash=data.get("live_geo_hash")
                )

            await websocket.send_json({
                "status": "received",
                "driver_id": driver_id
            })
    except WebSocketDisconnect:
        manager.disconnect_driver(websocket)
        print(f"Driver disconnected: {driver_id}")