from app import app, spider
from flask import jsonify

spider = spider.Spider()
heros = spider.getHeros()


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return jsonify(heros)


@app.route('/getMsg', methods=['GET'])
def home():

    response = {
        'name': 'Nirvazure',
        'hero': ['ganjiang', 'gongsunli', 'mozi']
    }
    return jsonify(response)
