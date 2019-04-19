from app import app, movie_recommand
from flask import render_template
from flask import jsonify, url_for


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    response = {
        'msg': "sdasdasdas"
    }
    return jsonify(response)


# 只获取整型ID
@app.route('/player/<int:player_id>')
def show_post(player_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % (player_id+1)

# url_for生成匹配url


@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')


@app.route('/getMsg', methods=['POST'])
def home():
    response = {
        'name': 'Nirvazure',
        'hero': ['ganjiang', 'gongsunli', 'mozi']
    }
    return jsonify(response)


@app.route('/search')
def search():
    user = {'nickname': 'Miguel'}  # fake user
    movie_name = 'Twelve Monkeys (1995)'
    posts = movie_recommand.web_api(movie_name, 15)
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)
