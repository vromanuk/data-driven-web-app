from flask import Blueprint, abort

from application.pypi_org.infrastructure.view_modifiers import response
from application.services import cms_service as cms_service

blueprint = Blueprint('cms', __name__, template_folder='templates')


@blueprint.route('/<path:full_url>')
@response(template_file='cms/page.html')
def cms_page(full_url: str):
    page = cms_service.get_page(full_url)
    if not page:
        abort(404, "Page doesn't exist")
    return page
