from cms.models.pluginmodel import CMSPlugin
from django.db import models
from enumfields import Enum
from enumfields import EnumField
from filer.fields.image import FilerImageField


class CardType(Enum):
    VERTICAL = 'vertical'
    HORIZONTAL = 'horizontal'


class CardsPerRow(Enum):
    TWO = '2'
    THREE = '3'


class CardListPluginModel(CMSPlugin):
    cards_per_row = EnumField(
        CardsPerRow,
        default=CardsPerRow.THREE,
        max_length=32,
    )

    def get_css_col_classes(self) -> str:
        if self.cards_per_row == CardsPerRow.THREE:
            return 'col-md-24 col-lg-8'
        elif self.cards_per_row == CardsPerRow.TWO:
            return 'col-md-24 col-lg-12'
        else:
            raise ValueError()

    def __str__(self):
        return f"({self.cards_per_row.value} per row)"


class CardPluginModel(CMSPlugin):
    image = FilerImageField(on_delete=models.PROTECT)
    title = models.CharField(max_length=1024, blank=True)
    type = EnumField(CardType, default=CardType.VERTICAL, max_length=32)

    def __str__(self):
        return self.title
