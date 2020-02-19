import os
import sys
import flask

from application.pypi_org.data import db_session as db_session

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

app = flask.Flask(__name__)


def main():
    register_blueprints()
    setup_db()
    app.run(debug=True)


def setup_db():
    db_file = os.path.join(
        os.path.dirname(__file__),
        'db',
        'pypi.sqlite')

    db_session.global_init(db_file)


def register_blueprints():
    from application.pypi_org.views import home_views
    from application.pypi_org.views import package_views
    from application.pypi_org.views import cms_views

    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(package_views.blueprint)
    app.register_blueprint(cms_views.blueprint)


if __name__ == '__main__':
    main()
