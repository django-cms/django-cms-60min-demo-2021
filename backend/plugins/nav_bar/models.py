from cms.models.pluginmodel import CMSPlugin
from django.db import models
from linkit.model_fields import LinkField


class NavBarPluginModel(CMSPlugin):
    is_full_width = models.BooleanField(
        default=False, verbose_name="Enable full-width mode",
    )
    is_enable_search_bar = models.BooleanField(
        default=True, verbose_name="Show search input",
    )
    is_use_default_menu = models.BooleanField(
        default=True,
        verbose_name="Use default menu",
        help_text=(
            "You can either use the default menu or compose a custom one "
            "by adding child Menu plugins inside this Navigation bar plugin"
        ),
    )
    is_use_multi_level_menu_on_mobile = models.BooleanField(
        default=False,
        verbose_name="Use multi-level menu on mobile",
        help_text="The multi-level menu shows around 3-4 levels of children."
    )

    def __str__(self):
        return ''


class MenuItemModel(CMSPlugin):
    link = LinkField(allow_target=True, allow_no_follow=True, types=['djangocms_blog', 'page', 'file', 'input'])
    
    def __str__(self) -> str:
        return self.link.label
