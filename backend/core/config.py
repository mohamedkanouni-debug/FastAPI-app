"""
core/config.py is the configuration file for the core package
so it contains all the configuration for the core package
an example of something that could be in this file is the database url 

in .env file you'll have :
DATABASE_URL = sqlite :///./database.db this is the url for the database
API_PREFIX=/api this is the prefix (meaning that the api will start with /api) for the api
DEBUG=True this is the debug mode for the api useful for development
ALLOWED_ORIGINS=https://localhost:3000,https://localhost:5173 this is the allowed origins for the api
OPENAI_API_KEY=

"""

from typing import List # use List to define a list (a List is used to define a list which is used to store data)
from pydantic_settings import BaseSettings
from pydantic import field_validator
 # use BaseSettings to define a base settings the reason why we define base settings is because we want to use pydantic to validate the settings
 # settings is a class that is used to store the settings
 # field_validator is used to validate the settings if the settings is not valid then it will raise an error if it is valid then it will return the settings to the user
 # the user needs to use the settings because the user needs to use the settings to connect to the database
 
class Settings(BaseSettings):
    DATABASE_URL: str
    API_PREFIX: str = "/api"
    DEBUG: bool = False
    ALLOWED_ORIGINS: str = ""
    OPENAI_API_KEY: str

    @field_validator("ALLOWED_ORIGINS")
    def parse_allowed_origins(cls, value: str) -> List[str]:
        return value.split(",") if value else []
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()


