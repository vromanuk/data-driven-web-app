from flask import Blueprint
from application.pypi_org.infrastructure.view_modifiers import response
from application.pypi_org.viewmodels.home.index_viewmodel import IndexViewModel
from application.pypi_org.viewmodels.shared.viewmodelbase import ViewModelBase

blueprint = Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    vm = IndexViewModel()
    return vm.to_dict()
    # return flask.render_template('home/index.html', packages=test_packages)


@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    vm = ViewModelBase()
    return vm.to_dict()

#
# @blueprint.route('/test')
# def test():
#     return package_service.test()
