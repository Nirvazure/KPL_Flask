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


@app.route('/herostype=<int:hero_type>', methods=['GET'])
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


@app.route('/rank', methods=['GET', 'POST'])
def api_rank():

    if request.method == 'GET':
        p_id = request.args.get('p_id')
        h_id = request.args.get('h_id')
        rank = request.args.get('rank')
        # 如果不为空才插入
        print(p_id, h_id, rank)
        rank_record = models.Rank(int(p_id), int(h_id), int(rank))
        db.session.add(rank_record)
        db.session.commit()
        # a = [rank for rank in ranks if rank['player']
        #      == p_id and rank['hero'] == h_id]
        # print(a['rank'])
        # print(p_id, h_id)
        # return jsonify(a)
        return "hhh"

    elif request.method == 'POST':
        # 不明白form为什么不可以
        p_id = request.json.get('p_id')
        h_id = request.json.get('h_id')
        rank = request.json.get('rank')
        print(p_id, h_id, rank)
        rank_record = models.Rank(int(p_id), int(h_id), int(rank))
        db.session.add(rank_record)
        db.session.commit()
        return "hhhh"


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
#     db.drop_all()
#     db.create_all()
#     players = [{'name': "SandM、影", 'summary': '上单霸主'}, {'name': "HyBarain", 'summary': '野区主宰'}, {
#         'name': "Nirvazure", 'summary': '中单法王'}, {'name': "甩葱的大叔", 'summary': '团队后盾'}, {'name': "TinyRed", 'summary': '国服AD'}]
#     for hero in heros:
#         herotemp = models.Hero(
#             hero['ename'], hero['cname'], hero['title'], hero['hero_type'], hero['color'])
#         db.session.add(herotemp)
#     for player in players:
#         playertemp = models.Player(player['name'], player['summary'])
#         db.session.add(playertemp)
#     db.session.commit()


# 创建表格、插入数据, 第一次请求完成，数据库创建好之后不需要了
