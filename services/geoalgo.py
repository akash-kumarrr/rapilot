import h3

def geohashing(longitude : float, latitude : float) -> str :
    return h3.latlng_to_cell(
        lat=latitude,
        lng=longitude,
        res=11
    )