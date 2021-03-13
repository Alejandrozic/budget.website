import os
from flask import Flask, url_for
# from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# login = LoginManager()
# login.login_view = 'auth.login'
db = SQLAlchemy()


from app.dashboard.views import dashboard_bp
from app.index.views import index_bp
from app.categories.views import categories_bp
from app.transactions.views import transactions_bp
from app.analysis.views import analysis_bp
from app.api.views import api_bp


def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config.DevConfig')

    db.init_app(app)
    with app.app_context():
        db.create_all()

    @app.template_filter('autoversion')
    def autoversion_filter(filename):
        full_path = os.path.join('app/', filename[1:])
        try:
            timestamp = str(int(os.path.getmtime(full_path)))
            return f"{filename}?v={timestamp}"
        except OSError:
            return filename

    # login.init_app(app)

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(index_bp)
    app.register_blueprint(categories_bp)
    app.register_blueprint(transactions_bp)
    app.register_blueprint(analysis_bp)
    app.register_blueprint(api_bp)

    return app
