from django.db import models
from filer.fields.file import FilerFileField
from parler.models import TranslatableModel
from parler.models import TranslatedFields
from solo.models import SingletonModel


class SiteConfig(SingletonModel, TranslatableModel):
    translations = TranslatedFields(
        site_name=models.CharField(max_length=1024),
        site_subname=models.CharField(
            max_length=1024,
            help_text="Shown in the navbar below the name.",
            blank=True,
        ),
    )
    logo = FilerFileField(
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name='site_config_logo',
        help_text="Logo on the navbar",
    )
    favicon = FilerFileField(
        blank=True, null=True, on_delete=models.PROTECT, related_name='site_config_favicon'
    )

    def __str__(self) -> str:
        return "Site Config"
