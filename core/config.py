from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    title : str 
    version : str 

    db_url : str

    jwt_secret_key : str 
    jwt_access_time : int 
    jwt_algorithm : str

    

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()