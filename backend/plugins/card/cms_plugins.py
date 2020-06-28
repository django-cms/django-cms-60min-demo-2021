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
    fieldsets = (
        (None, {
            'description': "You can add child plugins - content of this card - in the structure mode after saving the card list plugin.",
            'fields': [
                'image',
                'title',
                'internal_link',
                'external_link',
            ]
        }),
    )


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
    fieldsets = (
        (None, {
            'description': "You can add child plugins - content of this card - in the structure mode after saving the card list plugin.",
            'fields': [
                'cards_per_row',
            ]
        }),
    )
