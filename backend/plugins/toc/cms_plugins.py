from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from backend.plugins.default.module_name import MODULE_NAME


@plugin_pool.register_plugin
class TocPlugin(CMSPluginBase):
    module = MODULE_NAME
    name = _("Table of Contents")
    render_template = 'toc/toc-plugin.html'
