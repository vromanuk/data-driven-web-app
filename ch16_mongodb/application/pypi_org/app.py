import os
import sys
import flask

from application.pypi_org.nosql import mongo_setup
from application.pypi_org.nosql.users import User

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

app = flask.Flask(__name__)


def main():
    configure()
    app.run(debug=True)


def configure():
    print('Configuring Flask app: ')
    register_blueprints()
    print('Registered blueprints')
    setup_db()
    print('DB setup completed')
    print('', flush=True)


def setup_db():
    mongo_setup.global_init()


def register_blueprints():
    from application.pypi_org.views import home_views
    from application.pypi_org.views import package_views
    from application.pypi_org.views import cms_views
    from application.pypi_org.views import account_views

    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(package_views.blueprint)
    app.register_blueprint(cms_views.blueprint)
    app.register_blueprint(account_views.blueprint)


if __name__ == '__main__':
    main()
else:
    configure()
