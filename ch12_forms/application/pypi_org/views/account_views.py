from flask import Blueprint, request, redirect

from application.pypi_org.infrastructure.view_modifiers import response
from application.pypi_org.services import user_service

blueprint = Blueprint('account', __name__, template_folder='templates')


@blueprint.route('/account')
@response(template_file='account/index.html')
def index():
    return {}


@blueprint.route('/account/register', methods=['GET'])
@response(template_file='account/register.html')
def register_get():
    return {}


@blueprint.route('/account/register', methods=['POST'])
@response(template_file='account/register.html')
def register_post():
    req = request

    name = req.form.get('name')
    email = req.form.get('email', '').lower().strip()
    password = req.form.get('password', '').strip()

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

    return redirect('/account')


@blueprint.route('/account/login', methods=['GET'])
@response(template_file='account/login.html')
def login_get():
    return {}


@blueprint.route('/account/login', methods=['POST'])
@response(template_file='account/login.html')
def login_post():
    req = request

    email = req.form.get('email', '').lower().strip()
    password = req.form.get('password', '').strip()

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

    return redirect('/account')


@blueprint.route('/account/logout')
def logout():
    return {}
