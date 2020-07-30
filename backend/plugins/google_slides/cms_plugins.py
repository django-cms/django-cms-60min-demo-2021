from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from backend.plugins.google_slides.models import GoogleSlidesPluginModel
from backend.plugins.module_name import MODULE_NAME


@plugin_pool.register_plugin
class GoogleSlidesPlugin(CMSPluginBase):
    module = MODULE_NAME
    model = GoogleSlidesPluginModel
    name = "Google slides"
    render_template = 'google_slides/google_slides.html'
