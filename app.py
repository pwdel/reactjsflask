from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.apihandler import HelloApiHandler

# create instance of the flask class
# static_url is to specify a different path for static files
# static_folder points to the build directory of our react project
app = Flask(__name__, static_url_path='', static_folder='frontend/build')
# gets rid of CORS error when making API requests to different domain
CORS(app) #comment this on deployment
# put api handler in sub-directory called API
api = Api(app)

# @app.route decorator tells Flask which URL should trigger our serve(path) function.
@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

# put api in sub-directory called api
api.add_resource(HelloApiHandler, '/flask/hello')
