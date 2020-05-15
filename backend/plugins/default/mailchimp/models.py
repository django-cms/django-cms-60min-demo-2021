from cms.models.pluginmodel import CMSPlugin
from django.db import models


class MailchimpPluginModel(CMSPlugin):
    server_location_code = models.CharField(max_length=32, help_text="eg 'us18'")
    organization_id = models.CharField(max_length=1024)
    list_id = models.CharField(max_length=1024)
