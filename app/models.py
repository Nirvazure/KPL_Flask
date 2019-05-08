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
    hero_name = db.Column(db.String(80), unique=True)
    hero_title = db.Column(db.String(80), unique=True)
    hero_type = db.Column(db.String(20))
    hero_img = db.Column(db.String(80), unique=True)

    def __init__(self, hero_name, hero_title, hero_type, hero_img):
        self.hero_name = hero_name
        self.hero_type = hero_type
        self.hero_title = hero_title
        self.hero_img = hero_img
