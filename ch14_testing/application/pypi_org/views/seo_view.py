from flask import Blueprint

from application.pypi_org.infrastructure.view_modifiers import response
from application.pypi_org.viewmodels.seo.sitemap_viewmodel import SiteMapViewModel

blueprint = Blueprint('seo', __name__, template_folder='templates')


@blueprint.route('/sitemap.xml')
@response(mimetype='application/xml', template_file='seo/sitemap.html')
def sitemap():
    vm = SiteMapViewModel(1000)
    return vm.to_dict()


@blueprint.route('/robots.txt')
@response(mimetype='text/plain', template_file='seo/robots.txt')
def robots():
    return {}
