from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.safestring import mark_safe


class MailchimpPluginModel(CMSPlugin):
    server_location_code = models.CharField(max_length=32, help_text="eg 'us18'")
    organization_id = models.CharField(max_length=1024)
    list_id = models.CharField(max_length=1024)

    font_size = models.FloatField(default=1, help_text="In rem")
    width = models.CharField(max_length=512, default='100%', help_text="In css format, eg 350px or 100%")
    is_enable_border = models.BooleanField(default=True, verbose_name="Show input border")

    def get_html_style_attr(self) -> str:
        css = f'font-size: {self.font_size}rem !important; width: {self.width};'
        attr = f'style="{css}"'
        return mark_safe(attr)
