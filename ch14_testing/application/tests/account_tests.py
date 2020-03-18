"""
3 A's of test: Arrange, Act, then Assert
"""
from unittest.mock import patch

from application.pypi_org.data.users import User
from application.pypi_org.viewmodels.account.register_viewmodel import RegisterViewModel
from application.tests.test_client import flask_app


def test_register_validation_when_valid():
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


def test_register_validation_for_existing_user():
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
