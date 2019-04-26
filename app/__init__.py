

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['JSON_AS_ASCII'] = False
from app import views
