from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    These are read in the following order:
    env vars
    .env file
    
    Neither of which have been set up yet, I'm just adding placeholders
    """
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    
    db_uri: str = ""
    
    
settings = Settings()