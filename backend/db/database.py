from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from core.config import settings

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # sessionmaker is a class that is used to create a session it returns a session class

Base = declarative_base() # declarative_base() is a function that returns a base class for ORM models



def get_db():
    db = SessionLocal() # SessionLocal() is a function that is used to create a session 
    try:
        yield db
    finally:
        db.close()


def create_tables():
    Base.metadata.create_all(bind=engine)
