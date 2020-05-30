from cms.models import CMSPlugin
from django.core.management import BaseCommand
from django.db import transaction
from cms import api

from backend.plugins.default.heading_element.models import HeadingPlugin
from djangocms_bootstrap4.contrib.bootstrap4_heading.cms_plugins import Bootstrap4HeadingPlugin


class Command(BaseCommand):
    def handle(self, **options):
        with transaction.atomic():
            for instance_old in HeadingPlugin.objects.all():
                instance_old.delete()
                instance_new_data = dict(
                    name=instance_old.text,
                    tag=instance_old.heading_tag,
                    alignment=instance_old.heading_alignment,
                )
                instance_new: CMSPlugin = api.add_plugin(
                    placeholder=instance_old.placeholder,
                    plugin_type=Bootstrap4HeadingPlugin.__class__.__name__,
                    language=instance_old.language,
                    target=instance_old.parent,
                    **instance_new_data,
                )
                instance_new.position = instance_old.position
                instance_new.save()
