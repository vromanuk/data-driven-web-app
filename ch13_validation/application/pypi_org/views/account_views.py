from flask import Blueprint, request, redirect

from application.pypi_org.infrastructure import cookie_auth, request_dict
from application.pypi_org.infrastructure.view_modifiers import response
from application.pypi_org.services import user_service

blueprint = Blueprint('account', __name__, template_folder='templates')


@blueprint.route('/account')
@response(template_file='account/index.html')
def index():
    user_id = cookie_auth.get_user_id_via_auth_cookie(request)
    user = user_service.find_user_by_id(user_id)
    if not user:
        redirect('/account/login')
    return {
        'user': user
    }


@blueprint.route('/account/register', methods=['GET'])
@response(template_file='account/register.html')
def register_get():
    return {}


@blueprint.route('/account/register', methods=['POST'])
@response(template_file='account/register.html')
def register_post():
    data = request_dict.create(default_val='')

    name = data.name
    email = data.email.lower().strip()
    password = data.password.strip()

    if not (name or email or password):
        return {
            'name': name,
            'email': email,
            'password': password,
            'error': "Some required fields are missing."
        }
    user = user_service.create_user(name, email, password)
    if not user:
        return {
            'name': name,
            'email': email,
            'password': password,
            'error': "A user with that email already exists."
        }
    resp = redirect('/account')
    cookie_auth.set_auth(resp, user.id)
    return resp


@blueprint.route('/account/login', methods=['GET'])
@response(template_file='account/login.html')
def login_get():
    return {}


@blueprint.route('/account/login', methods=['POST'])
@response(template_file='account/login.html')
def login_post():
    data = request_dict.create()

    email = data.email.lower().strip()
    password = data.password.strip()

    if not (email or password):
        return {
            'email': email,
            'password': password,
            'error': "Some required fields are missing."
        }

    user = user_service.login_user(email, password)
    if not user:
        return {
            'email': email,
            'password': password,
            'error': "The account doesn't exist or the password is wrong."
        }
    resp = redirect('/account')
    cookie_auth.set_auth(resp, user.id)
    return resp


@blueprint.route('/account/logout')
def logout():
    resp = redirect('/')
    cookie_auth.logout(resp)

    return resp
