from flask import Flask


def run_app():
    app = Flask(__name__)

    from app.routes import api
    app.register_blueprint(api, url_prefix="/api")

    return app
