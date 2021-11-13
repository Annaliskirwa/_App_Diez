from . import db

class Quotes(db.Model):
    __tablename__ = "quotes"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    message = db.Column(db.String())
    #creator

    def __repr__(self):
        return f'Quotes {self.title}'

class Comment(db.Model):
    __tablename__ = "usercomments"
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String())
    #commentor 

class User(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))