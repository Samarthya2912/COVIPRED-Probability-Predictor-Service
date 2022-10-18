import pandas as pd
import pickle
from Features import getFeatures
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

def predictSeverityFromDataframe(df):
    df = df[features]
    filename = config['model']
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model.predict(df)

def predictSeverityFromDict(dict):
    df = pd.DataFrame(dict, index=[0])
    return predictSeverityFromDataframe(df)
