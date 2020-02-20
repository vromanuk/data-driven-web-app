from flask import Blueprint, request, redirect

from application.pypi_org.infrastructure import cookie_auth, request_dict
from application.pypi_org.infrastructure.view_modifiers import response
from application.pypi_org.services import user_service
from application.pypi_org.viewmodels.account.index_viewmodel import IndexViewModel
from application.pypi_org.viewmodels.account.register_viewmodel import RegisterViewModel

blueprint = Blueprint('account', __name__, template_folder='templates')


@blueprint.route('/account')
@response(template_file='account/index.html')
def index():
    vm = IndexViewModel()
    if not vm.user:
        redirect('/account/login')
    return vm.to_dict()


@blueprint.route('/account/register', methods=['GET'])
@response(template_file='account/register.html')
def register_get():
    vm = RegisterViewModel()
    return vm.to_dict()


@blueprint.route('/account/register', methods=['POST'])
@response(template_file='account/register.html')
def register_post():
    vm = RegisterViewModel()
    vm.validate()

    if vm.error:
        return vm.to_dict()

    user = user_service.create_user(vm.name, vm.email, vm.password)
    if not user:
        vm.error = 'The account could not be created.'
        return vm.to_dict()

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
