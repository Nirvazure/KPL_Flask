from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
CORS(app, supports_credentials=True)
app.config['JSON_AS_ASCII'] = False
from app import views
# from app import view1
