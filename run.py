from flask import Flask, session
from flask_migrate import Migrate

import config
from database import db
from src.models.user import User
from src.utils import logger


def createApp():
    '''
        - Creates flask app
        - Setups db
    '''
    app = Flask(__name__, template_folder="src/templates")
    app.config.from_object(config)
    db.init_app(app)
    migrate = Migrate(app, db)
    return app


def registerBlueprints(app):
    '''
        - Registers blueprint for provided app
    '''
    from src.http.controllers.default import defaultBp
    app.register_blueprint(defaultBp, url_prefix="/")


def registerContextProcessor(app):
    @app.context_processor
    def injectExtraConfig():
        '''
            - Puts extra config values to be used in templates
        '''
        return {}

    @app.context_processor
    def injectUser():
        '''
            - Puts user(logged in) in context to be used in templates
        '''
        doesCtxUserExists = "userId" in session
        ctxUser = User.query.filter_by(fbId = session.get("userId", None)).first().serialize() if doesCtxUserExists else None
        return {
            "doesCtxUserExists": doesCtxUserExists,
            "ctxUser": ctxUser
        }


if __name__ == "__main__":
    app = createApp()
    registerBlueprints(app)
    registerContextProcessor(app)
    app.run()
