from flask import Flask
from flask_restful import Api
from dal import DBInterface
import resources


app = Flask(__name__)
api = Api(app)

api.add_resource(resources.KeyGenerator, resources.KeyGenerator.custom_url)
api.add_resource(resources.KeyCounter, resources.KeyCounter.custom_url)
api.add_resource(resources.KeyManager, resources.KeyManager.custom_url)

if __name__ == '__main__':
    app.run(debug=True)
    DBInterface().create_tables()
