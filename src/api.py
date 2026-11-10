from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from db import get_last_prediction

app = FastAPI()

@app.get("/prediction")
def prediction(city: str):
    row = get_last_prediction(city)
    if row is None:
        raise HTTPException(status_code=404, detail="No hay predicciones para esa ciudad")
    return row

@app.get("/")
def home():
    return FileResponse("static/index.html")