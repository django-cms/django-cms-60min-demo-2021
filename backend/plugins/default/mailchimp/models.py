from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.safestring import mark_safe


class MailchimpPluginModel(CMSPlugin):
    font_size = models.FloatField(default=1, help_text="In rem")
    server_location_code = models.CharField(max_length=32, help_text="eg 'us18'")
    organization_id = models.CharField(max_length=1024)
    list_id = models.CharField(max_length=1024)

    def get_html_style_attr(self) -> str:
        html = f'style="font-size: {self.font_size}rem !important;"'
        return mark_safe(html)
