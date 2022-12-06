import pickle
from models.user_profile_model import UserProfileModel, PredictionResponse

class PredictionModelService:
    def __init__(self) -> None:
        with open('config/placement_prediction_model_v2.pkl', 'rb') as file:
            self.model = pickle.load(file)

    def predict(self, data: UserProfileModel) -> PredictionResponse:
        user_info = list(data.__dict__.values())
        res = self.model.predict([user_info[1:]])
        return PredictionResponse(uid=data.uid,prediction=res)
        