from fastapi import FastAPI
from routes.healthcheck import router as health_router
from routes.forecastRoute import router as parse_forecast_input

app = FastAPI()

#System health check route
app.include_router(health_router)

#Read forecast input route
app.include_router(parse_forecast_input,prefix = "/api")


@app.get("/")
def greeting():
    return {"status":200,"success":True}