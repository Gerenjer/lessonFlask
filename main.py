from flask import Flask
from config import _config
from db_settings import db
from routes import api

def create_app():
    app = Flask(__name__)
    app.config.from_object(_config)
    db.init_app(app)
    app.register_blueprint(api, url_prefix='/api')
    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context(): 
        db.create_all()
    app.run(debug=True)