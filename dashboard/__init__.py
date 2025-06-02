from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    db.init_app(app)
    login_manager.init_app(app)

    from .routes import dashboard_bp
    app.register_blueprint(dashboard_bp)

    # إضافة API
    try:
        from api.endpoints import api_bp
        app.register_blueprint(api_bp, url_prefix='/api')
    except ImportError:
        pass

    return app
