from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

Mirakuru = FastAPI()

@Mirakuru.get("/")
def main():
    return FileResponse("index.html")

Mirakuru.mount("/", StaticFiles(directory= "D:\\code\\kursovaya"), name = "kursovaya")
