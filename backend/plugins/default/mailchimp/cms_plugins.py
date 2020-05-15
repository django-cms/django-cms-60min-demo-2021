from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from backend.plugins.default.mailchimp.models import MailchimpPluginModel
from backend.plugins.default.module_name import MODULE_NAME


@plugin_pool.register_plugin
class MailchimpPlugin(CMSPluginBase):
    module = MODULE_NAME
    model = MailchimpPluginModel
    name = _("Mailchimp Subscription Form")
    render_template = 'mailchimp/mailchimp_plugin.html'
