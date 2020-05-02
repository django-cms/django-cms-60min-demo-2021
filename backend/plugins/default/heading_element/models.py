from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.text import slugify
from enumfields import Enum
from enumfields import EnumField


class HeadingType(Enum):
    STANDARD = 'standard'


class HeadingTag(Enum):
    H1 = 'h1'
    H2 = 'h2'
    H3 = 'h3'
    H4 = 'h4'
    H5 = 'h5'
    H6 = 'h6'
    DIV = 'div'
    P = 'p'


class HeadingColor(Enum):
    DARK = 'dark'
    WHITE = 'white'
    BLUE = 'blue'


class HeadingAlignment(Enum):
    LEFT = 'left'  # .text-left
    CENTER = 'center'  # .text-center
    RIGHT = 'right'


class HeadingPlugin(CMSPlugin):
    text = models.CharField(max_length=2048)

    heading_tag = EnumField(HeadingTag, default=HeadingTag.H1, max_length=32)
    heading_color = EnumField(HeadingColor, default=HeadingColor.DARK, max_length=32)
    heading_alignment = EnumField(HeadingAlignment, default=HeadingAlignment.LEFT, max_length=32)

    def get_anchor(self) -> str:
        return slugify(self.text)

    def __str__(self) -> str:
        if self.text:
            return self.text
        return ""
