from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.template.defaultfilters import safe
from django.utils.translation import ugettext_lazy as _

from backend.plugins.mailchimp.models import MailchimpPluginModel
from backend.plugins.module_name import MODULE_NAME


@plugin_pool.register_plugin
class MailchimpPlugin(CMSPluginBase):
    module = MODULE_NAME
    model = MailchimpPluginModel
    name = _("Newsletter Subscription (Mailchimp)")
    render_template = 'mailchimp/mailchimp_plugin.html'
    fieldsets = [
        (None, {
            'description': safe("""
                In order to find that data:
                <ol>
                    <li>Login into your mailchimp account</li>
                    <li>In the top menu click <b>Audience</b> and select <b>Signup forms</b> item</li>
                    <li>Click on <b>Embedded forms</b></li>
                    <li>Find the <b>Copy/paste onto your site</b> section</li>
                </ol>
                <p></p>
                <p>There you will see an HTML snippet, find the tag &lt;form&gt; there.</p>
                <p>It will look as &lt;form action='https://effectiefaltruisme.<b>us14</b>.list-manage.com/subscribe/post?u=<b>0d235948217a55858a0e810c4</b>&amp;id=<b>d652eb1a9c</b>'&gt;. 
                Here <b>us14</b> is your server location code, <b>0d235948217a55858a0e810c4</b> is your organization id and <b>d652eb1a9c</b> is your list id.</p>
            """),
            'fields': (
                'server_location_code',
                'organization_id',
                'list_id',
            )
        }),
    ]
