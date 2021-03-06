from flask_login import UserMixin

from app.run import db


class User(UserMixin, db.Model):
    """
    User Mdoel
    """
    __tablename__ = 'tb_user'
    uid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(60), unique=True)
    password = db.Column(db.String(200), default="")

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_id(self):
        return self.uid

    def __repr__(self):
        return '<User %r>' % self.username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False


