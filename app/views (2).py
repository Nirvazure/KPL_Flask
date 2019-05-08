from app import db, app, models, spider
from flask import jsonify, render_template, url_for, request

# spider = spider.Spider()

# @app.before_first_request
# def create_db():
#     heros = spider.getHeros()
#   # Recreate database each time for demo
#   # db.drop_all()
#     db.create_all()
#     for hero in heros:
#         herotemp = models.Hero(hero['name'], hero['title'],
#                                hero['type'], hero['src'])
#         db.session.add(herotemp)
#     db.session.commit()
# 创建表格、插入数据,第一次请求完成，数据库创建好之后不需要了

#     guestes = [models.User('guest1', 'guest1@example.com'),
#                models.User('guest2', 'guest2@example.com'),
#                models.User('guest3', 'guest3@example.com'),
#                models.User('guest4', 'guest4@example.com')]
#     db.session.add_all(guestes)


@app.route('/heros')
def heros():
    heros = models.Hero.query.all()
    return "<br>".join(["{0}: {1}:{2}:{3}".format(hero.hero_name, hero.hero_title, hero.hero_type, hero.hero_img) for hero in heros])


@app.route('/heros/<int:id>')
def hero(id):
    hero = models.Hero.query.filter_by(id=id).one()
    return "<br>".join(["{0}: {1}:{2}:{3}".format(hero.hero_name, hero.hero_title, hero.hero_type, hero.hero_img)])

#
