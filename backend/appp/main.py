from fastapi import FastAPI
from prediction import prediction
from schema import sms_input
from fastapi.responses import JSONResponse

app = FastAPI(title="SMS Spam Classifier API")

@app.get("/")
def home():
    return {"Homepage of Email/SMS Spam Classifier"}

@app.get("/health", tags=["Health"])
def health_check():
    """
    Returns the health status of the service.
    """
    return JSONResponse(content={"status": "ok", "message": "Backend is healthy"})

@app.post("/predict")
def prediction_api(request:sms_input):
    predicted = prediction(request.message)
    if predicted == 1:
        label = 'Spam'
    else:
        label = 'Not Spam'
    return {'prediction':label}
