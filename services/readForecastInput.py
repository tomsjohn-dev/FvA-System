import pandas as pd

def readForecastInput(data:dict):

    try:
        forecastInputDf = pd.DataFrame([data])
        return {"status":200,"success":True,"message":"Successfully read Data"}
    except Exception as e:
        print("Service Error :",e)
        return {"status":500,"success":False,"message":"Error is reading the input"}