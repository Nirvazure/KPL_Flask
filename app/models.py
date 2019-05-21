from app import db

# player_hero = db.Table('player_hero',
#                        db.Column('player_id', db.Integer, db.ForeignKey(
#                            'player.id'), primary_key=True),
#                        db.Column('hero_id', db.Integer, db.ForeignKey(
#                            'hero.id'), primary_key=True),
#                        db.Column('rank', db.Integer))


class Player(db.Model):

    __tablename__ = 'player'

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.String(80), unique=True)
    summary = db.Column(db.String(240))
    # player_hero = db.relationship('Hero', secondary=player_hero,
    #                               backref=db.backref('players'))

    def __init__(self, name, summary):
        self.name = name
        self.summary = summary


class Hero(db.Model):

    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    title = db.Column(db.String(80), unique=True)
    hero_type = db.Column(db.String(20))
    img = db.Column(db.String(80), unique=True)
    color = db.Column(db.String(80))

    def __init__(self, id, name, title, type_id, color):
        hero_type = {1: '战士', 2: '法师', 3: '坦克',
                     4: '刺客', 5: '射手', 6: '辅助', }
        self.id = id
        self.name = name
        self.title = title
        self.hero_type = hero_type[type_id]
        self.img = "https://game.gtimg.cn/images/yxzj/img201606/heroimg/" + \
            str(id)+"/"+str(id)+".jpg"
        self.color = color


class Rank(db.Model):

    p_id = db.Column(db.Integer, db.ForeignKey('player.id'),  primary_key=True)
    h_id = db.Column(db.Integer, db.ForeignKey('hero.id'), primary_key=True)
    rank = db.Column(db.Integer)
    level = db.Column(db.Integer)

    def __init__(self, p_id, h_id, rank):
        self.p_id = p_id
        self.h_id = h_id
        self.rank = rank
