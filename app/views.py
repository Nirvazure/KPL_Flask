from app import spider, app, db, models
from flask import jsonify, render_template, url_for, request


@app.route('/heros/<int:id>')
def hero(id):
    hero = models.Hero.query.filter_by(id=id).one()
    return "<br>".join(["{0}: {1}:{2}:{3}".format(hero.hero_name, hero.hero_title, hero.hero_type, hero.hero_img)])


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return 'KPL'


@app.route('/heros', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_hero():
    if request.method == 'GET':
        heros = []
        items = models.Hero.query.all()
        for item in items:
            hero = {}
            hero['id'] = item.id
            hero['name'] = item.name
            hero['img'] = item.img
            hero['type'] = item.hero_type
            hero['title'] = item.title
            heros.append(hero)
        return jsonify(heros)

    elif request.method == 'POST':
        # return jsonify(heros1)
        return "ECHO: PACTH\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"


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


@app.route('/player/<int:player_id>')
def show_post(player_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % (player_id+1)

# url_for生成匹配url


@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')


# @app.before_first_request
# def create_db():

#     sp = spider.Spider()
#     heros = sp.getHeros()
#   # Recreate database each time for demo
#   # db.drop_all()
#     db.create_all()
#     for hero in heros:
#         herotemp = models.Hero(
#             hero['ename'], hero['cname'], hero['title'], hero['hero_type'])
#         db.session.add(herotemp)
#     db.session.commit()
# 创建表格、插入数据,第一次请求完成，数据库创建好之后不需要了

# guestes = [models.User('guest1', 'guest1@example.com'),
#            models.User('guest2', 'guest2@example.com'),
#            models.User('guest3', 'guest3@example.com'),
#            models.User('guest4', 'guest4@example.com')]
# db.session.add_all(guestes)
