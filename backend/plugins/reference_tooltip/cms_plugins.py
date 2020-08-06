from cms.plugin_pool import plugin_pool
from djangocms_text_ckeditor.cms_plugins import TextPlugin

from backend.plugins.module_name import MODULE_NAME


@plugin_pool.register_plugin
class ReferenceTooltipPlugin(TextPlugin):
    module = MODULE_NAME
    name = "Reference tooltip"
    render_template = 'reference_tooltip/reference_tooltip_plugin.html'
    text_enabled = True
