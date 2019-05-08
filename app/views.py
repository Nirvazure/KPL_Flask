from app import spider, app
from flask import jsonify, render_template, url_for

spider = spider.Spider()
heros = spider.getHeros()


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    # return jsonify(heros)
    return 'KPL'


# @app.route('/', methods=['GET','POST'])
# def getHeros():
#     return jsonify(heros)

@app.route('/heros', methods=['GET'])
def getHeros():
    return jsonify(heros)


@app.route('/search')
def search():
    user = {'nickname': 'Miguel'}  # fake user
    # movie_name = 'Twelve Monkeys (1995)'
    # posts = movie_recommand.web_api(movie_name, 15)
    return render_template("index.html",
                           title='Home',
                           user=user,
                           #    posts=posts
                           )

# 只获取整型ID


@app.route('/player/<int:player_id>')
def show_post(player_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % (player_id+1)

# url_for生成匹配url


@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')
