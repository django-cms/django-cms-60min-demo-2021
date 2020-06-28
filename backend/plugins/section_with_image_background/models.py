from cms.models.pluginmodel import CMSPlugin
from django.db import models
from enumfields import Enum
from enumfields import EnumField
from filer.fields.image import FilerImageField


class RichTextEditorBackground(Enum):
    WHITE = 'white'
    BLACK = 'black'
    GRAY = 'gray'


class SectionWithImageBackgroundPluginModel(CMSPlugin):
    name = models.CharField(max_length=512, help_text="For displaying in the plugin tree")
    background_image = FilerImageField(
        on_delete=models.PROTECT,
        help_text="Minimal width is 1920px, default minimal height is 350px, but can be configured below."
    )
    height = models.IntegerField(default=350, help_text="In pixels")
    rich_text_editor_background = EnumField(
        RichTextEditorBackground,
        default=RichTextEditorBackground.WHITE,
        help_text=(
            "You can set the background of a rich text editor used inside this plugin, for readability purposes. "
            "For example if your background image is black it's better to set background in the editor to be black as well."
        ),
    )

    def get_size(self) -> str:
        return f'2560x{self.height}'

    def __str__(self):
        if self.name:
            return self.name
        return ''
