from app import db
import enum
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from app import login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(34), unique=True)
    password = db.Column(db.String(256))
    pets = db.relationship('Pet', backref='owner', lazy='dynamic')
    info_ = db.relationship('Info', backref = ' ' , uselist=False, lazy='select')
    def __init__(self,login,password):
        self.login = login
        self.password = generate_password_hash(password)
    def __repr__(self):
        return "{} {} {}".format(self.id, self.login, self.password)
    def set_password(self,password):
        self.password = generate_password_hash(password)
    def check_password(self,password):
        return check_password_hash(self.password, password)

class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(34))
    age = db.Column(db.Integer,)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12))
    type = db.Column(db.Integer, db.ForeignKey('types.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
        return "{} {}".format(self.name)

class Types(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(12))
    pets = db.relationship('Pet', backref='typepet', lazy='dynamic')
    def __repr__(self):
        return self.type
