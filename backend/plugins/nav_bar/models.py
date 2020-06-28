from cms.models.pluginmodel import CMSPlugin
from django.db import models


class NavBarPluginModel(CMSPlugin):
    is_full_width = models.BooleanField(
        default=False, verbose_name="Full width",
    )
    is_enable_search_bar = models.BooleanField(
        default=True, verbose_name="Show search input",
    )

    def __str__(self):
        return ''
