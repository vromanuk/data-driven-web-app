from flask import Blueprint, request

from application.pypi_org.infrastructure import cookie_auth
from application.pypi_org.infrastructure.view_modifiers import response
from application.pypi_org.services import package_service, user_service

blueprint = Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    return {
        'releases': package_service.get_latest_releases(),
        'package_count': package_service.get_package_count(),
        'release_count': package_service.get_release_count(),
        'user_count': user_service.get_user_count(),
        'user_id': cookie_auth.get_user_id_via_auth_cookie(request)
    }
    # return flask.render_template('home/index.html', packages=test_packages)


@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    return {
        'user_id': cookie_auth.get_user_id_via_auth_cookie(request)
    }

#
# @blueprint.route('/test')
# def test():
#     return package_service.test()
