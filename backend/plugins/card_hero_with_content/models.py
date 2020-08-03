from cms.models import CMSPlugin
from enumfields import Enum
from enumfields import EnumField


class VerticalSpacing(Enum):
    SMALL = 'small'
    NORMAL = 'normal'
    LARGE = 'large'
    
    class Labels:
        SMALL = "Small (30px)"
        NORMAL = "Normal (60px)"
        LARGE = "Large (100px)"


class VerticalAlignment(Enum):
    TOP = 'top'
    MIDDLE = 'middle'
    BOTTOM = 'bottom'


class HeroElementSize(Enum):
    SMALL = 'small'
    NORMAL = 'normal'
    LARGE = 'large'

    class Labels:
        SMALL = "Small - 41%"
        NORMAL = "Normal - 50%"
        LARGE = "Large - 62%"


class CardHeroWithContent(CMSPlugin):
    vertical_spacing = EnumField(VerticalSpacing, default=VerticalSpacing.SMALL, max_length=32)
    vertical_alignment = EnumField(VerticalAlignment, default=VerticalAlignment.MIDDLE, max_length=32)
    hero_element_size = EnumField(HeroElementSize, default=HeroElementSize.NORMAL, max_length=32)

    def get_hero_col_classes(self) -> str:
        if self.hero_element_size == HeroElementSize.SMALL:
            return 'col-24 col-md-10'
        elif self.hero_element_size == HeroElementSize.NORMAL:
            return 'col-24 col-md-12'
        elif self.hero_element_size == HeroElementSize.LARGE:
            return 'col-24 col-md-15'

    def get_content_col_classes(self) -> str:
        if self.hero_element_size == HeroElementSize.SMALL:
            return 'col-24 col-md-14'
        elif self.hero_element_size == HeroElementSize.NORMAL:
            return 'col-24 col-md-12'
        elif self.hero_element_size == HeroElementSize.LARGE:
            return 'col-24 col-md-9'
