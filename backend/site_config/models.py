from django.db import models
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

    def __str__(self) -> str:
        return "Site Config"
