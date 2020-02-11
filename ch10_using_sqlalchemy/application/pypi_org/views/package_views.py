from flask import Blueprint

blueprint = Blueprint('packages', __name__, template_folder='templates')


@blueprint.route('/project/<package_name>')
def package_details(package_name: str):
    return f"Package details for {package_name}"


@blueprint.route('/<int:rank>')
def popular(rank: int):
    return f"The details for {rank}th most popular package"
