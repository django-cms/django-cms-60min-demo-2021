from cms.models import CMSPlugin
from django.db import models


class GoogleSlidesPluginModel(CMSPlugin):
    name = models.CharField(
        max_length=256,
        help_text="For admins only - displayed in the plugins sidebar",
        blank=True,
    )
    link = models.URLField(
        help_text="In order to get this link open your presentation and in the menu select File -> Publish to the web"
    )
    width = models.CharField(
        max_length=32, default='100%', help_text="In pixels (500px) or percentages"
    )
    height = models.CharField(
        max_length=32, default='550px', help_text="In pixels or percentages"
    )

    def __str__(self) -> str:
        if self.name:
            return self.name
        else:
            return ''

    def get_link(self) -> str:
        return self.link.replace('/pub?', '/embed?')

    def get_delay_in_ms(self) -> float:
        return self.delay * 1000
