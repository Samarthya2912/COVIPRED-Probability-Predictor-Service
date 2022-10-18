from Predictor import *
import pandas as pd

dict = {'cough': 1, 'fever': 1, 'sore_throat': 0, 'shortness_of_breath': 1,
            'head_ache': 1, 'age_60_and_above': 1, 'gender': 0, 'test_indication': 1}
print(predictInfectionProbabilityFromDict(dict))
