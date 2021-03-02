from typing import List

from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.utils.plugins import get_plugin_model
from django.utils.translation import ugettext_lazy as _

from backend.plugins.module_name import MODULE_NAME
from backend.plugins.section_with_image_background.models import (
    SectionWithImageBackgroundPluginModel,
)


@plugin_pool.register_plugin
class SectionWithImageBackgroundPlugin(CMSPluginBase):
    model = SectionWithImageBackgroundPluginModel
    module = MODULE_NAME
    name = _("Section with image background")
    render_template = 'section_with_image_background/section_with_image_background.html'
    allow_children = True
    css_class_name = 'section-with-image-background-plugin'

    fieldsets = (
        (
            None,
            {
                'description': "You can add plugins inside this plugin, eg a text or heading plugin.",
                'fields': [
                    'name',
                    'background_image',
                    'height',
                    'background_effect',
                    'background_effect_color',
                    'background_effect_opacity',
                ],
            },
        ),
    )

    @classmethod
    def get_child_ckeditor_body_css_class(cls, plugin: CMSPlugin) -> str:
        plugin_model = get_plugin_model(plugin.plugin_type)
        instance: SectionWithImageBackgroundPluginModel = plugin_model.objects.get(pk=plugin.pk)
        classes: List[str] = []
        if instance.background_effect:
            classes.append(f'{cls.css_class_name}--effect--{instance.background_effect.value}')
            if instance.background_effect_color:
                classes.append(
                    f'{cls.css_class_name}--effect-color--{instance.background_effect_color.value}'
                )
        return ' '.join(classes)
