from cms.models.pluginmodel import CMSPlugin
from django.db import models
from filer.fields.image import FilerImageField
from parler.models import TranslatableModel
from parler.models import TranslatedFields


class PersonListPluginModel(CMSPlugin):
    title = models.CharField(max_length=2048, blank=True)

    def __str__(self) -> str:
        if self.title:
            return self.title
        return ''


class Person(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=1024),
        description=models.CharField(max_length=1024, blank=True),
    )
    photo = FilerImageField(on_delete=models.PROTECT)
    link = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class PersonPluginModel(CMSPlugin):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        help_text=(
            "The person record that's attached to this plugin is global, "
            "ie if you change a photo of a person it's going to change on all related Person plugins"
        ),
    )

    def copy_relations(self, old_instance: 'PersonPluginModel'):
        self.person = old_instance.person

    def __str__(self) -> str:
        return self.person.name
