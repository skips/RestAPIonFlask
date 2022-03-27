from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Board(db.Model):
    __tablename__ = "board"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)

    def __init__(self, name):
        self.name = name


class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id', ondelete='CASCADE'), nullable=False)
    board = db.relationship('Board', backref=db.backref('note', lazy='dynamic'))

    def __init__(self, name, content, board_id):
        self.name = name
        self.content = content
        self.board_id = board_id
