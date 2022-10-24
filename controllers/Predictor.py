from flask_restful import Resource, reqparse
from getFeatures import getFeatures
from Predictors import predictInfectionFromDict, predictInfectionProbabilityFromDict


class Predictor(Resource):
    def get(self):
        return {'message': 'Predictor route working!'}

    def post(self):
        parser = reqparse.RequestParser()
        features = getFeatures()
        for feature in features:
            parser.add_argument(feature, type=int)
        args = parser.parse_args()
        # print(args)
        return {
            'probability': predictInfectionProbabilityFromDict(args),
            'infected': (int)(predictInfectionFromDict(args))
        }
