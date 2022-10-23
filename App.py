from flask import Flask
from flask_restful import Resource, Api, reqparse
from Predictors import predictInfectionProbabilityFromDict
from getFeatures import getFeatures
from controllers.Home import Home
from controllers.Predictor import Predictor

app = Flask(__name__)
api = Api(app)

api.add_resource(Home, '/')
api.add_resource(Predictor, '/predictor')

if __name__ == '__main__':
    app.run(debug=True)