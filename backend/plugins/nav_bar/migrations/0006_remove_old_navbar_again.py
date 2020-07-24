from cms.models import CMSPlugin
from django.db import migrations


def drop_old_navbar_from_header_placeholder(apps, _):
    CMSPlugin.objects.filter(placeholder__slot__iexact='header', plugin_type='NavBarPlugin').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('nav_bar', '0005_remove_old_navbar'),
    ]

    operations = [
        migrations.RunPython(drop_old_navbar_from_header_placeholder),
    ]
