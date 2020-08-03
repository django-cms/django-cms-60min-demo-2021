from cms.models import CMSPlugin
from enumfields import Enum
from enumfields import EnumField


class CardSpacing(Enum):
    SMALL = 'small'
    NORMAL = 'normal'
    LARGE = 'large'
    
    class Labels:
        SMALL = "Small (30px)"
        NORMAL = "Normal (75px)"
        LARGE = "Large (100px)"


class VerticalAlignment(Enum):
    TOP = 'top'
    MIDDLE = 'middle'
    BOTTOM = 'bottom'


class ContentWrapperSize(Enum):
    SMALL = 'small'
    NORMAL = 'normal'
    LARGE = 'large'

    class Labels:
        SMALL = "Small ~35%"
        NORMAL = "Normal ~50%"
        LARGE = "Large ~60%"


class CardHeroWithContent(CMSPlugin):
    spacing = EnumField(CardSpacing, default=CardSpacing.SMALL, max_length=32)
    vertical_alignment = EnumField(VerticalAlignment, default=VerticalAlignment.MIDDLE, max_length=32)
    content_wrapper_size = EnumField(ContentWrapperSize, default=ContentWrapperSize.NORMAL, max_length=32)
    
    _col_size = 24
    _col_content_large = 14
    _col_content_normal = 12
    _col_content_small = 9
    _col_bp = 'xl'

    def get_hero_col_classes(self) -> str:
        col_size_rel = self._col_size
        if self.spacing != CardSpacing.SMALL:
            col_size_rel -= 1

        if self.content_wrapper_size == ContentWrapperSize.SMALL:
            return f'col-{self._col_size} col-{self._col_bp}-{col_size_rel - self._col_content_small}'
        elif self.content_wrapper_size == ContentWrapperSize.NORMAL:
            return f'col-{self._col_size} col-{self._col_bp}-{col_size_rel - self._col_content_normal}'
        elif self.content_wrapper_size == ContentWrapperSize.LARGE:
            return f'col-{self._col_size} col-{self._col_bp}-{col_size_rel - self._col_content_large}'

    def get_content_col_classes(self) -> str:
        if self.content_wrapper_size == ContentWrapperSize.SMALL:
            return f'col-{self._col_size} col-{self._col_bp}-{self._col_content_small}'
        elif self.content_wrapper_size == ContentWrapperSize.NORMAL:
            return f'col-{self._col_size} col-{self._col_bp}-{self._col_content_normal}'
        elif self.content_wrapper_size == ContentWrapperSize.LARGE:
            return f'col-{self._col_size} col-{self._col_bp}-{self._col_content_large}'
