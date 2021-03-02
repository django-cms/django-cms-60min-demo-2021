from cms.models import CMSPlugin
from django.db import models


class GoogleSheetPluginModel(CMSPlugin):
    name = models.CharField(
        max_length=256,
        help_text="For admins only - displayed in the plugins sidebar",
        blank=True,
    )
    link = models.URLField(
        help_text="In order to get this link open your sheet and in the menu select File -> Publish to the web"
    )
    width = models.CharField(
        max_length=32, default='100%', help_text="In pixels (500px) or percentages"
    )
    height = models.CharField(
        max_length=32, default='721px', help_text="In pixels or percentages"
    )
    is_show_headers = models.BooleanField(default=False, verbose_name="Show table headers")

    def __str__(self) -> str:
        if self.name:
            return self.name
        else:
            return ''

    def get_link(self) -> str:
        return f'{self.link}?widget=true&amp;headers={str(self.is_show_headers).lower()}'

    def get_delay_in_ms(self) -> float:
        return self.delay * 1000
