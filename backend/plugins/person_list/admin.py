from django.contrib import admin
from django.contrib.admin import ModelAdmin
from parler.admin import TranslatableAdmin

from backend.plugins.person_list.models import Person


@admin.register(Person)
class Person(TranslatableAdmin, ModelAdmin):
    list_display = [
        'name',
        'description',
        'link',
    ]
