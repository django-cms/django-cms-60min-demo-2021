from cms import api
from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib.admin.helpers import AdminForm
from django.http import HttpRequest
from django.utils.translation import ugettext_lazy as _

from backend.plugins.card_hero_with_content.models import CardHeroWithContent
from backend.plugins.module_name import MODULE_NAME


@plugin_pool.register_plugin
class CardHeroWithContentPlugin(CMSPluginBase):
    module = MODULE_NAME
    name = _("Hero card with content (2 columns)")
    model = CardHeroWithContent
    render_template = 'card_hero_with_content/card_hero_with_content_plugin.html'
    allow_children = True
    child_classes = [
        'CardHeroWrapperPlugin',
        'CardContentWrapperPlugin',
    ]

    @classmethod
    def get_empty_change_form_text(cls, obj=None):
        return "You can add child plugins - to content and hero cards - in the structure mode after saving this plugin."

    def save_model(self, request: HttpRequest, obj: CMSPlugin, form: AdminForm, change: bool):
        super().save_model(request, obj, form, change)

        is_create_action = not change
        if is_create_action:
            self._create_child_plugins()

    def _create_child_plugins(self):
        hero_wrapper: CMSPlugin = api.add_plugin(
            placeholder=self.saved_object.placeholder,
            plugin_type='CardHeroWrapperPlugin',
            language=self.saved_object.language,
            target=self.saved_object,
        )
        hero_wrapper.save()

        content_wrapper: CMSPlugin = api.add_plugin(
            placeholder=self.saved_object.placeholder,
            plugin_type='CardContentWrapperPlugin',
            language=self.saved_object.language,
            target=self.saved_object,
        )
        content_wrapper.save()


@plugin_pool.register_plugin
class CardHeroWrapperPlugin(CMSPluginBase):
    module = MODULE_NAME
    name = _("Hero wrapper")
    render_template = 'card_hero_with_content/hero_wrapper_plugin.html'
    require_parent = True
    parent_classes = [
        'CardHeroWithContentPlugin',
    ]
    allow_children = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        setattr(self.model, '__str__', lambda e: '')


@plugin_pool.register_plugin
class CardContentWrapperPlugin(CMSPluginBase):
    module = MODULE_NAME
    name = _("Content wrapper")
    render_template = 'card_hero_with_content/content_wrapper_plugin.html'
    require_parent = True
    parent_classes = [
        'CardHeroWithContentPlugin',
    ]
    allow_children = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        setattr(self.model, '__str__', lambda e: '')
