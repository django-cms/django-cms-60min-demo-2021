# Generated by Django 2.2.14 on 2020-08-03 15:20

import backend.plugins.card_hero_with_content.models
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardHeroWithContent',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='card_hero_with_content_cardherowithcontent', serialize=False, to='cms.CMSPlugin')),
                ('vertical_spacing', enumfields.fields.EnumField(default='small', enum=backend.plugins.card_hero_with_content.models.CardSpacing, max_length=32)),
                ('vertical_alignment', enumfields.fields.EnumField(default='middle', enum=backend.plugins.card_hero_with_content.models.VerticalAlignment, max_length=32)),
                ('hero_element_size', enumfields.fields.EnumField(default='normal', enum=backend.plugins.card_hero_with_content.models.ContentWrapperSize, max_length=32)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
