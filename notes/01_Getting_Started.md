# Recent Work

Just  recently got done with the following React App, which we can derive this codebase from:

* [reactjs - buy/sell indicator functionality](https://github.com/pwdel/dockerreactjs)

Our objective is to integrate a flask app in with this React functionality, to be able to later connect machine learning functionality in order to send a buy/sell signal.

Additional features may include performance indicators and dashboards showing how the trading strategy may have performed over a particular time period.

## Getting Started!

Typically in the past we have opted not to build virtual environments and send requirements.txt to Dockerfiles, but rather to build said requirements.txt files manually so as to be careful about which dependencies are being used and to minimize dependencies.

The project structure advised in [1] is the following:

![](/readme_img/starterprojectstructure.png)

### Building Out Simple Flask App

```
om flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.HelloApiHandler import HelloApiHandler

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
api.add_resource(apihandler, '/flask/hello')
```


### CORS Errors

At this current stage (before deployment), React is running on port 3000 and Flask on port 5000. Hence, when React is making a request to Flask backend, this CORS error pops up.


### API Handler



### Installing and Working with Flask

#### Running flask

```
flask run
```

#### Checking Installation

http://127.0.0.1:5000/flask/hello


#### requirements.txt File

flask-restful - for api handling
flask_cors
flask

#  References

* [How to Deploy a React+Flask App](https://towardsdatascience.com/build-deploy-a-react-flask-app-47a89a5d17d9)
