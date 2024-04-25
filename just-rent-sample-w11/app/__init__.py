from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    from app.models.user import User
    return User.query.get(int(user_id))

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # 當未經身份驗證的用戶嘗試訪問需要登入的頁面時，將重定向到 controllers.admin_login 所對應的 URL。
    login_manager.login_view = 'controller.admin_login'

    from app.controllers import bp as controllers_bp
    app.register_blueprint(controllers_bp)

    from app.models import bp as models_bp
    app.register_blueprint(models_bp)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp)

    return app
