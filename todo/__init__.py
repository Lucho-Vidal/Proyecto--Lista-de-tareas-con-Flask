import os

from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='mikey',
        DATABASE_HOST=os.environ.get('FLASK_DATABESE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABESE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABESE_USER'),
        DATABASE=os.environ.get('FLASK_DATABESE')
    )

    from . import db

    db.init_app(app)


    @app.route('/hola')
    def hola():
        return 'Chanchito Feliz'
    
    return app