from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from backend.plugins.module_name import MODULE_NAME


@plugin_pool.register_plugin
class FooterPlugin(CMSPluginBase):
    name = "Footer"
    module = MODULE_NAME
    render_template = 'footer/footer_plugin.html'
    allow_children = True
    child_ckeditor_body_css_class = 'footer-plugin'
