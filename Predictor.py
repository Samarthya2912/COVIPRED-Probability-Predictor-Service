import pandas as pd
import pickle
import sys
from Features import getFeatures

features = getFeatures()

def predictInfectionProbabilityFromDataframe(df):
    df = df[features]
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model.predict_proba(df)[0][1]

def predictInfectionProbabilityFromDict(dict):
    df = pd.DataFrame(dict, index=[0])
    return predictInfectionProbabilityFromDataframe(df)

def predictSeverityFromDataframe(df):
    df = df[features]
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model.predict(df)

def predictSeverityFromDict(dict):
    df = pd.DataFrame(dict, index=[0])
    return predictSeverityFromDataframe(df)
