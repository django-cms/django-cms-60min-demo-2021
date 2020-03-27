from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from backend.plugins.default.module_name import MODULE_NAME
from backend.plugins.default.section_with_image_background.models import SectionWithImageBackgroundPluginModel


@plugin_pool.register_plugin
class SectionWithImageBackgroundPlugin(CMSPluginBase):
    model = SectionWithImageBackgroundPluginModel
    module = MODULE_NAME
    name = _("Section with image background")
    render_template = 'section_with_image_background/section_with_image_background.html'
    allow_children = True
