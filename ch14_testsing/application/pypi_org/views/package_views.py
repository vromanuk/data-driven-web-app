from flask import Blueprint, abort

from application.pypi_org.infrastructure.view_modifiers import response
from application.pypi_org.viewmodels.packages.pagedetails_viewmodel import PackageDetailsViewModel

blueprint = Blueprint('packages', __name__, template_folder='templates')


@blueprint.route('/project/<package_name>')
@response(template_file='packages/details.html')
def package_details(package_name: str):
    vm = PackageDetailsViewModel(package_name)
    if not vm.package:
        return abort(status=404)

    return vm.to_dict()


@blueprint.route('/<int:rank>')
def popular(rank: int):
    return f"The details for {rank}th most popular package"
