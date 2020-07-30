from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from backend.plugins.google_sheet.models import GoogleSheetPluginModel
from backend.plugins.module_name import MODULE_NAME


@plugin_pool.register_plugin
class GoogleSheetPlugin(CMSPluginBase):
    module = MODULE_NAME
    model = GoogleSheetPluginModel
    name = "Google sheet"
    render_template = 'google_sheet/google_sheet.html'
