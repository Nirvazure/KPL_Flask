from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email


class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    title = db.Column(db.String(80), unique=True)
    hero_type = db.Column(db.String(20))
    img = db.Column(db.String(80), unique=True)

    def __init__(self, id, name, title, type_id):
        hero_type = {1: '战士', 2: '法师', 3: '坦克',
                     4: '刺客', 5: '射手', 6: '辅助', }
        self.id = id
        self.name = name
        self.title = title
        self.hero_type = hero_type[type_id]
        self.img = "https://game.gtimg.cn/images/yxzj/img201606/heroimg/" + \
            str(id)+"/"+str(id)+".jpg"
