from fastapi import FastAPI
from prediction import prediction
from schema import sms_input

app = FastAPI(title="SMS Spam Classifier API")

@app.get("/")
def home():
    return {"Homepage of Email/SMS Spam Classifier"}

@app.get("/health")
def health():
    return {'status':200,
            'version':1}

@app.post("/predict")
def prediction_api(request:sms_input):
    predicted = prediction(request.message)
    if predicted == 1:
        label = 'Spam'
    else:
        label = 'Not Spam'
    return {'prediction':label}
