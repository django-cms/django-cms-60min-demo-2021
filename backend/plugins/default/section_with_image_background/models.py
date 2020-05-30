from cms.models.pluginmodel import CMSPlugin
from django.db import models
from filer.fields.image import FilerImageField


class SectionWithImageBackgroundPluginModel(CMSPlugin):
    name = models.CharField(max_length=512, help_text="For displaying in the plugin tree")
    background_image = FilerImageField(
        on_delete=models.PROTECT,
        help_text="Minimal width is 1920px, default minimal height is 350px, but can be configured below."
    )
    height = models.IntegerField(default=350, help_text="In pixels")

    def get_size(self) -> str:
        return f'2560x{self.height}'

    def __str__(self):
        if self.name:
            return self.name
        return ''
