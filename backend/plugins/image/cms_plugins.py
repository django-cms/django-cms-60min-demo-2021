from cms.plugin_pool import plugin_pool
from link_all.cms_plugins import LinkAllPlugin

from backend.plugins.image.models import ImagePluginModel
from backend.plugins.module_name import MODULE_NAME


@plugin_pool.register_plugin
class ImagePlugin(LinkAllPlugin):
    module = MODULE_NAME
    model = ImagePluginModel
    name = "Picture / Image (scalable)"
    render_template = 'image/image_plugin.html'
    text_enabled = False
    change_form_template = 'link_all/admin/link_all.html'
    fieldsets = [
        (None, {
            'fields': [
                'image',
                'alignment',
                'thumbnail_config',
                'is_full_screen_on_click',
                'vertical_spacing',
            ],
        }),
        ("Link", {
            'classes': ['collapse'],
            'fields': [
                'link_all_field',
                'link_label',
                'link_type',
                'link_instance_pk',
                'link_url',
            ],
        }),
    ]
