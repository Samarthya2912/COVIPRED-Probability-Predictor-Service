import pandas as pd
import pickle
from getFeatures import getFeatures
from config import config

features = getFeatures()

def predictInfectionProbabilityFromDataframe(df):
    df = df[features]
    filename = config['model']
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model.predict_proba(df)[0][1]

def predictInfectionProbabilityFromDict(dict):
    df = pd.DataFrame(dict, index=[0])
    return predictInfectionProbabilityFromDataframe(df)

def predictInfectionFromDataframe(df):
    df = df[features]
    filename = config['model']
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model.predict(df)[0]

def predictInfectionFromDict(dict):
    df = pd.DataFrame(dict, index=[0])
    return predictInfectionFromDataframe(df)
