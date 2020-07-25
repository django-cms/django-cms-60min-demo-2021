# Generated by Django 2.2.14 on 2020-07-25 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section_with_image_background', '0003_add_field_background_effect'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sectionwithimagebackgroundpluginmodel',
            name='rich_text_editor_background',
        ),
        migrations.AddField(
            model_name='sectionwithimagebackgroundpluginmodel',
            name='background_effect_opacity',
            field=models.CharField(blank=True, default='50%', help_text='eg 50%', max_length=32),
        ),
    ]
