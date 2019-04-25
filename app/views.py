from app import app
from flask import jsonify
#!/usr/bin/python


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    response = {
        'msg': "sdasdasdas"
    }
    return jsonify(response)


@app.route('/getMsg', methods=['GET'])
def home():

    response = {
        'name': 'Nirvazure',
        'hero': ['ganjiang', 'gongsunli', 'mozi']
    }
    return jsonify(response)
