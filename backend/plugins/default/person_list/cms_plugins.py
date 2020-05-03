from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from backend.plugins.default.module_name import MODULE_NAME
from backend.plugins.default.person_list.models import PersonListPluginModel
from backend.plugins.default.person_list.models import PersonPluginModel


@plugin_pool.register_plugin
class PersonListPlugin(CMSPluginBase):
    module = MODULE_NAME
    name = _("Person list")
    model = PersonListPluginModel
    render_template = 'person_list/person-list-plugin.html'
    child_classes = ['PersonPlugin']
    allow_children = True


@plugin_pool.register_plugin
class PersonPlugin(CMSPluginBase):
    module = MODULE_NAME
    name = _("Person")
    model = PersonPluginModel
    render_template = 'person_list/person-plugin.html'
    parent_classes = ['PersonContainerPlugin']
