from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('settings/config.py') 
CORS(app) 
db = SQLAlchemy(app)


#import Views and Routes
from app.views.userViews import *
from app.views.apiViews import *


if __name__ == "__main__":
    app.run(debug=True)