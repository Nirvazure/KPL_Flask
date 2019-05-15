from app import spider, app, db, models
from flask import jsonify, render_template, url_for, request


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return 'KPL'


# @app.route('/recommands', methods=['GET'])
# def api_recommand():
#     sp = spider.Spider()
#     heros = sp.getHeros()
#     return jsonify(heros[0:4])


@app.route('/heros/type<int:hero_type>', methods=['GET'])
@app.route('/heros', methods=['GET'])
def api_heros(hero_type=None):
    if request.method == 'GET':
        if(hero_type != None):
            heros = []
            type_dict = {1: '战士', 2: '法师', 3: '坦克',
                         4: '刺客', 5: '射手', 6: '辅助', }
            items = models.Hero.query.filter_by(
                hero_type=type_dict[hero_type]).all()
            for item in items:
                hero = {}
                hero['id'] = item.id
                hero['name'] = item.name
                hero['img'] = item.img
                hero['type'] = item.hero_type
                hero['title'] = item.title
                hero['color'] = item.color
                heros.append(hero)
        else:
            heros = []
            items = models.Hero.query.all()
            for item in items:
                hero = {}
                hero['id'] = item.id
                hero['name'] = item.name
                hero['img'] = item.img
                hero['type'] = item.hero_type
                hero['title'] = item.title
                hero['color'] = item.color
                heros.append(hero)
        return jsonify(heros)


@app.route('/heros/<int:hero_id>', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_hero(hero_id):

    if request.method == 'GET':
        item = models.Hero.query.filter_by(id=hero_id).one()
        hero = {}
        hero['id'] = item.id
        hero['name'] = item.name
        hero['img'] = item.img
        hero['type'] = item.hero_type
        hero['title'] = item.title
        hero['color'] = item.color
        return jsonify(hero)

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
#             hero['ename'], hero['cname'], hero['title'], hero['hero_type'], hero['color'])
#         db.session.add(herotemp)
#     db.session.commit()
# 创建表格、插入数据,第一次请求完成，数据库创建好之后不需要了
