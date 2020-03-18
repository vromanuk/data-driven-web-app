from flask import Blueprint, abort

from application.pypi_org.infrastructure.view_modifiers import response
from application.pypi_org.viewmodels.cms.page_viewmodel import PageViewModel

blueprint = Blueprint('cms', __name__, template_folder='templates')


@blueprint.route('/<path:full_url>')
@response(template_file='cms/page.html')
def cms_page(full_url: str):
    vm = PageViewModel(full_url)

    if not vm.page:
        abort(404, "Page doesn't exist")
    return vm.to_dict()
