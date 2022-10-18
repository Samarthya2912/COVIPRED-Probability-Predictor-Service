import sys

def getFeatures():
    features = ['cough', 'fever', 'sore_throat', 'shortness_of_breath',
            'head_ache', 'age_60_and_above', 'gender', 'test_indication']
    return features

sys.modules['getFeatures'] = getFeatures