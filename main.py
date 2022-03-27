from flask import Flask, Blueprint
from flask_restful import Api
from models import db
from views import BoardsList, BoardAPI, NotesList, NoteAPI

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://teachmeuser:23091994@localhost/test_api_db'

    db.init_app(app)

    with app.app_context():
        db.create_all()
        db.session.commit()

    app.register_blueprint(api_bp, url_prefix='/api/v1/')
    return app


api.add_resource(BoardsList, '/board')
api.add_resource(BoardAPI, '/board/<int:id_board>')
api.add_resource(NotesList, '/note')
api.add_resource(NoteAPI, '/note/<int:id_note>')


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
