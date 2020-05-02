from cms.models.pluginmodel import CMSPlugin
from django.db import models
from filer.fields.image import FilerImageField


class PersonListPluginModel(CMSPlugin):
    title = models.CharField(max_length=2048, blank=True)

    def __str__(self) -> str:
        if self.title:
            return self.title
        return ''


class PersonPluginModel(CMSPlugin):
    name = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024, blank=True)
    photo = FilerImageField(on_delete=models.PROTECT)
    link = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
