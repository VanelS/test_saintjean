from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Charger le modèle entraîné avec Joblib
model = joblib.load('logistic_regression_model.joblib')


# Créer l'application FastAPI
app = FastAPI()

# Définir le modèle de données pour la requête (entrées de l'utilisateur)
class PassengerData(BaseModel):
    Pclass: int
    Sex: int  # 0 pour homme, 1 pour femme
    Age: float
    Fare: float
    Embarked: int  # 0 = Cherbourg, 1 = Queenstown, 2 = Southampton

# Endpoint pour vérifier si l'API est en ligne
@app.get("/")
def read_root():
    return {"message": "API Titanic Model is online"}

# Endpoint pour faire des prédictions
@app.post("/predict/")
def predict_survival(data: PassengerData):
    # Convertir les données en dataframe pour la prédiction
    input_data = pd.DataFrame([data.dict()])

    # Faire la prédiction avec le modèle
    prediction = model.predict(input_data)

    # Retourner le résultat de la prédiction
    if prediction[0] == 1:
        return {"prediction": "Le passager aurait survécu"}
    else:
        return {"prediction": "Le passager n'aurait pas survécu"}
