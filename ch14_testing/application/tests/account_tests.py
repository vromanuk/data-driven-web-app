"""
3 A's of test: Arrange, Act, then Assert
"""
from unittest.mock import patch

from flask import Response

from application.pypi_org.data.users import User
from application.pypi_org.viewmodels.account.register_viewmodel import RegisterViewModel
from application.tests.test_client import flask_app, client


def test_vm_register_validation_when_valid():
    # Arrange
    form_data = {
        'name': 'Vlad',
        'email': 'vroma@gmail.com',
        'password': 'test' * 6
    }
    with flask_app.test_request_context(path='/account/register', data=form_data):
        vm = RegisterViewModel()

    # Act
    target = 'application.pypi_org.services.user_service.find_user_by_email'
    with patch(target, return_value=None):
        vm.validate()

    # Assert
    assert vm.error is None


def test_vm_register_validation_for_existing_user():
    # Arrange
    form_data = {
        'name': 'Vlad',
        'email': 'vroma@gmail.com',
        'password': 'test' * 6
    }
    with flask_app.test_request_context(path='/account/register', data=form_data):
        vm = RegisterViewModel()

    # Act
    target = 'application.pypi_org.services.user_service.find_user_by_email'
    test_user = User(email=form_data.get('email'))
    with patch(target, return_value=test_user):
        vm.validate()

    # Assert
    assert vm.error is not None
    assert 'already exists' in vm.error


@patch('application.pypi_org.services.user_service.find_user_by_email', return_value=None)
@patch('application.pypi_org.services.user_service.create_user', return_value=User())
def test_v_register_view_new_user(mock_find_user_by_email, mock_create_user):
    from application.pypi_org.views.account_views import register_post
    # Arrange
    form_data = {
        'name': 'Vlad',
        'email': 'vroma@gmail.com',
        'password': 'test' * 6
    }
    # Act
    with flask_app.test_request_context(path='/account/register', data=form_data):
        resp: Response = register_post()
    # Assert
    assert resp.location == '/account'
    assert mock_find_user_by_email.called is True
    assert mock_create_user.called is True


def test_integration_account_home_no_login(client):
    target = 'application.pypi_org.services.user_service.find_user_by_id'
    with patch(target, return_value=None):
        response: Response = client.get('/account')

    assert response.status_code == 302
    assert '/account/login' in response.location


def test_integration_account_home_with_login(client):
    target = 'application.pypi_org.services.user_service.find_user_by_id'
    test_user = User(name='Vlad', email='vroma@gmail.com')
    with patch(target, return_value=test_user):
        response: Response = client.get('/account')

    assert response.status_code == 200
    assert b'Vlad' in response.data
