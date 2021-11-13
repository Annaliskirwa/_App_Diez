from . import db

class Quotes(db.Model):
    __tablename__ = "quotes"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    message = db.Column(db.String())
    #creator

class Comment:
    id
    comment 
    commentor 

class User:
    id
    name