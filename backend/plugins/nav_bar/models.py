from cms.models.pluginmodel import CMSPlugin
from django.db import models
from enumfields import Enum


class NavBarType(Enum):
    SMALL = 'small'
    NORMAL = 'normal'
    
    class Labels:
        SMALL = 'Full-width, short and fixed on top of the screen'
        NORMAL = 'Normal'


class NavBarPluginModel(CMSPlugin):
    is_full_width = models.BooleanField(
        default=False, verbose_name="Full width",
    )
    is_enable_search_bar = models.BooleanField(
        default=True, verbose_name="Show search input",
    )

    def __str__(self):
        return ''
