from os import name

from flask.typing import TemplateFilterCallable


class Quotes:
    id
    name
    title 
    message 
    creator

class Comment:
    id
    comment 
    commentor 

class User:
    id
    name