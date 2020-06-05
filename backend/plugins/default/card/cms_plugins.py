from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from backend.plugins.default.card.models import CardListPluginModel
from backend.plugins.default.card.models import CardPluginModel
from backend.plugins.default.module_name import MODULE_NAME


@plugin_pool.register_plugin
class CardPlugin(CMSPluginBase):
    module = MODULE_NAME
    name = _("Card")
    model = CardPluginModel
    render_template = 'card/card-plugin.html'
    allow_children = True


@plugin_pool.register_plugin
class CardListPlugin(CMSPluginBase):
    module = MODULE_NAME
    name = _("Card list")
    model = CardListPluginModel
    render_template = 'card/card-list-plugin.html'
    allow_children = True
    child_classes = [
        'CardPlugin',
    ]
