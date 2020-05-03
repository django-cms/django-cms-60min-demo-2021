from django.db import models
from filer.fields.image import FilerImageField


class Event(models.Model):
    name = models.CharField(max_length=2048)
    location = models.CharField(max_length=2048)
    image = FilerImageField(on_delete=models.PROTECT)
    
    teaser_description = models.TextField()
    description = models.TextField()
    
    signup_url = models.URLField()
