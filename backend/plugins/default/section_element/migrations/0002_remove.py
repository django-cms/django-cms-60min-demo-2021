from cms import api
from cms.models import CMSPlugin
from django.db import migrations

from backend.plugins.default.section_element.models import SectionPlugin
from djangocms_bootstrap4.contrib.bootstrap4_grid.cms_plugins import Bootstrap4GridContainerPlugin


def migrate_to_bs4_container(apps, _):
    for instance_old in SectionPlugin.objects.all():
        instance_old.delete()
        instance_new_data = dict(
            name=instance_old.name,
        )
        instance_new: CMSPlugin = api.add_plugin(
            placeholder=instance_old.placeholder,
            plugin_type=Bootstrap4GridContainerPlugin.__class__.__name__,
            language=instance_old.language,
            target=instance_old.parent,
            **instance_new_data,
        )
        instance_new.position = instance_old.position
        instance_new.save()



class Migration(migrations.Migration):
    dependencies = [
        ('section_element', '0001_initial'),
    ]


    operations = [
        migrations.RunPython(migrate_to_bs4_container),
    ]
