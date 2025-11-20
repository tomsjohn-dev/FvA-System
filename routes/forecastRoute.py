from fastapi import APIRouter

router = APIRouter()

@router.post('/forecast')
def fetch_forecast_input(data:dict):

    print("API hit")
    print("Received:", data)
    
    return {"status":200,"data":data}