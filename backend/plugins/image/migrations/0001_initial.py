# Generated by Django 2.2.14 on 2020-07-31 12:22

import backend.plugins.image.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('filer', '0011_auto_20190418_0137'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagePluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='image_imagepluginmodel', serialize=False, to='cms.CMSPlugin')),
                ('link_instance_pk', models.PositiveIntegerField(blank=True, null=True)),
                ('link_url', models.CharField(blank=True, max_length=1024)),
                ('link_label', models.CharField(blank=True, help_text='You can leave it empty to use the default object label, eg the page name', max_length=1024)),
                ('alignment', enumfields.fields.EnumField(default='center', enum=backend.plugins.image.models.ImageAlignment, max_length=64)),
                ('is_full_screen_on_click', models.BooleanField(default=True, verbose_name='Open full screen modal on click')),
                ('vertical_spacing', enumfields.fields.EnumField(blank=True, default='extra_small', enum=backend.plugins.image.models.ImageVerticalSpacing, max_length=32, null=True)),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, to=settings.FILER_IMAGE_MODEL)),
                ('link_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType')),
                ('thumbnail_config', models.ForeignKey(blank=True, help_text='When set the image is going to be cropped / scaled up to the provided dimensions.', null=True, on_delete=django.db.models.deletion.PROTECT, to='filer.ThumbnailOption', verbose_name='Thumbnail config')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin', models.Model),
        ),
    ]
