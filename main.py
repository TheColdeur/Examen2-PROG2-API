from typing import List
import fastapi
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import Response, JSONResponse


app = FastAPI()

Characteristics: BaseModel = {
    max_speed: int,
    max_fuel_capacity: int
}

Car: BaseModel = {
    identifier: str,
    brand: str,
    model: str,
    characteristics: Characteristics
}

cars: List[Car] = []

@app.get("/ping")
def pong():
    return Response(content="pong", status_code=200, media_type="text/plain")

@app.post("/cars")
def createCars(list_car: List[Car]):
    cars.extend(list_car)
    list_car_json = []
    for car in cars:
        list_car_json.append(car.model.dump())
    return JSONResponse(content=list_car_json, status_code=201, media_type="application/json")

@app.get("/cars")
def getAllCars():
    list_car_json = []
    for car in cars:
        list_car_json.append(car.model.dump())
    return JSONResponse(content=list_car_json, status_code=200, media_type="application/json")

@app.get("/cars/{id}")
def getCarById(id: int):
    for car in cars:
        if id == car.id:
            return JSONResponse(content=car, status_code=200, media_type="application/json")
    return Response(content="Not found", status_code=404)