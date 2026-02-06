from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings

app = FastAPI(
    title="choose your own adventure game" ,
    description="api to generate stories" ,
    version='0.1.0',
    docs_url='/docs', #this means that the docs will be available at http://127.0.0.1:8000/docs
    redoc_url='/redoc', #this means that the redoc will be available at http://127.0.0.1:8000/redoc




)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,  # allow_origins=settings.ALLOWED_ORIGINS means that the frontend can access the backend
    allow_credentials=True, # this means that the frontend can send cookies , cookies are used to authenticate the user by the backend 
    allow_methods=["*"], # allows all methods which are GET , POST , PUT , DELETE
    allow_headers=["*"], # allows all headers which are content-type , authorization
    # cookies are defined as headers in the frontend 
)

if __name__ == "__main__":  # this means that if the file is run as a script then run the uvicorn server 
    import uvicorn # this imports the uvicorn server which used to run the server
    uvicorn.run( "main:app", host="0.0.0.0", port=8000, reload=True) # "main:app" means that the file (main.py) is run as a script  

