from flask import Flask
from flask_restful import Resource, Api, reqparse
from Predictor import predictInfectionProbabilityFromDict
from Features import getFeatures

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return { 'message': 'Hello World!' }

class Predictor(Resource):
    def get(self): 
        return { 'message': 'Predictor route working!' }

    def post(self):
        parser = reqparse.RequestParser()
        features = getFeatures()
        for feature in features:
            parser.add_argument(feature, type=int)
        args = parser.parse_args()    
        print(args)
        return { 'prediction': predictInfectionProbabilityFromDict(args) }    
         

api.add_resource(Home, '/')
api.add_resource(Predictor, '/predictor')

if __name__ == '__main__':
    app.run(debug=True)