from django.db import models
from enumfields import EnumField
from parler.models import TranslatableModel
from parler.models import TranslatedFields
from solo.models import SingletonModel

from backend.plugins.nav_bar.models import NavBarType


class SiteConfig(SingletonModel, TranslatableModel):
    translations = TranslatedFields(
        site_name=models.CharField(max_length=1024),
        site_subname=models.CharField(
            max_length=1024,
            help_text="Shown in the navbar below the name.",
            blank=True,
        ),
    )
    navbar_default = EnumField(
        NavBarType,
        default=NavBarType.NORMAL,
        help_text="The type of navbar that will be set on newly created pages",
    )

    def __str__(self) -> str:
        return "Site Config"
