from flask import request
from flask_restful import Resource
from models import db, Board, Note
from schemas import BoardSchema, NoteSchema

board_schema = BoardSchema()
boards_schema = BoardSchema(many=True)
note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)
notes_join_schema = NoteSchema(many=True, only=("id", "name", "content"))


class BoardsList(Resource):
    @staticmethod
    def get():
        try:
            all_boards = Board.query.all()
            db.session.commit()
            result = boards_schema.dump(all_boards)
        except Exception:
            db.session.rollback()
            raise
        return result

    @staticmethod
    def post():
        try:
            json_data = board_schema.load(request.get_json(force=True))
            board = Board(**json_data)
            db.session.add(board)
            db.session.commit()
            result = board_schema.dump(board)
        except Exception:
            db.session.rollback()
            raise
        return result, 201


class BoardAPI(Resource):
    @staticmethod
    def get(id_board):
        try:
            board = Board.query.filter_by(id=id_board).first()
            db.session.commit()
            board_result = board_schema.dump(board)
            notes_result = notes_join_schema.dump(board.note.all())
        except Exception:
            db.session.rollback()
            raise
        return {"board": board_result, "notes": notes_result}


class NotesList(Resource):
    @staticmethod
    def get():
        try:
            all_notes = Note.query.all()
            db.session.commit()
            result = notes_schema.dump(all_notes)
        except Exception:
            db.session.rollback()
            raise
        return result

    @staticmethod
    def post():
        try:
            json_data = note_schema.load(request.get_json(force=True))
            note = Note(**json_data)
            db.session.add(note)
            db.session.commit()
            result = note_schema.dump(note)
        except Exception:
            db.session.rollback()
            raise
        return result, 201


class NoteAPI(Resource):
    @staticmethod
    def get(id_note):
        try:
            one_note = Note.query.filter_by(id=id_note).first()
            db.session.commit()
            result = note_schema.dump(one_note)
        except Exception:
            db.session.rollback()
            raise
        return result
