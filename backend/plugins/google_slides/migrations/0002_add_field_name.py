# Generated by Django 2.2.14 on 2020-07-30 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google_slides', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='googleslidespluginmodel',
            name='name',
            field=models.CharField(blank=True, help_text='For admins only - displayed in the plugins sidebar', max_length=256),
        ),
        migrations.AlterField(
            model_name='googleslidespluginmodel',
            name='height',
            field=models.CharField(default='721px', help_text='In pixels or percentages', max_length=32),
        ),
        migrations.AlterField(
            model_name='googleslidespluginmodel',
            name='link',
            field=models.URLField(help_text='In order to get this link open your presentation and in the menu select File -> Publish to the web'),
        ),
    ]