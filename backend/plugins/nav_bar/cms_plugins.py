from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from link_all.cms_plugins import LinkButtonPlugin

from backend.plugins.module_name import MODULE_NAME
from backend.plugins.nav_bar.models import MenuItemModel
from backend.plugins.nav_bar.models import NavBarPluginModel


@plugin_pool.register_plugin
class NavBarPlugin(CMSPluginBase):
    module = MODULE_NAME
    name = _("Navigation Bar")
    model = NavBarPluginModel
    render_template = 'nav_bar/nav_bar.html'
    allow_children = True
    child_classes = [
        'MenuItemPlugin',
    ]


@plugin_pool.register_plugin
class MenuItemPlugin(LinkButtonPlugin):
    module = MODULE_NAME
    name = "Menu Item"
    model = MenuItemModel
    render_template = 'nav_bar/menu_item.html'
    parent_classes = [
        'NavBarPlugin',
    ]
