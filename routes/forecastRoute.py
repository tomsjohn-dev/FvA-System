from fastapi import APIRouter
from controllers.forecastController import parseForecastInput

router = APIRouter()

@router.post('/forecast')
def fetch_forecast_input(data:dict):

    return parseForecastInput(data)
    