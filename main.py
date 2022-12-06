from fastapi import FastAPI
from models.user_profile_model import UserProfileModel, PredictionResponse
from services.prediction_model_service import PredictionModelService

app = FastAPI()

predictionService : PredictionModelService = None

@app.on_event('startup')
def startup():
    print("Initializing ML Model")
    global predictionService 
    predictionService = PredictionModelService()
    print("Initialized")

@app.get("/")
def root():
    return "Hello World!"

@app.post("/predict", response_model=PredictionResponse)
def prediction(data: UserProfileModel):
    return predictionService.predict(data)