from cms.models.pluginmodel import CMSPlugin
from django.db import models
from enumfields import Enum
from enumfields import EnumField
from filer.fields.image import FilerImageField


class RichTextEditorBackground(Enum):
    WHITE = 'white'
    BLACK = 'black'
    GRAY = 'gray'


class BackgroundEffect(Enum):
    COLOR = 'color'
    GRADIENT = 'gradient'
    COLOR_WITH_GRADIENT = 'color_with_gradient'


class BackgroundEffectColor(Enum):
    PRIMARY = 'primary'
    SECONDARY = 'secondary'


class SectionWithImageBackgroundPluginModel(CMSPlugin):
    name = models.CharField(max_length=512, help_text="For displaying in the plugin tree")
    background_image = FilerImageField(
        on_delete=models.PROTECT,
        help_text="Minimal width is 1920px, default minimal height is 350px, but can be configured below.",
    )
    height = models.IntegerField(default=350, help_text="In pixels")

    background_effect = EnumField(
        BackgroundEffect,
        default=None,
        blank=True,
        null=True,
        help_text="Can be applied on top of the image",
        max_length=32,
    )
    background_effect_color = EnumField(
        BackgroundEffectColor,
        default=BackgroundEffectColor.PRIMARY,
        max_length=32,
        blank=True,
        null=True,
    )
    background_effect_opacity = models.CharField(
        max_length=32, default='50%', help_text="eg 50%", blank=True
    )

    def get_size(self) -> str:
        return f'2560x{self.height}'

    def __str__(self):
        if self.name:
            return self.name
        return ''
