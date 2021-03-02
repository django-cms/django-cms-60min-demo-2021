from cms.plugin_pool import plugin_pool
from djangocms_bootstrap4.contrib.bootstrap4_link.cms_plugins import Bootstrap4LinkPlugin
from djangocms_bootstrap4.contrib.bootstrap4_picture.cms_plugins import Bootstrap4PicturePlugin
from djangocms_bootstrap4.contrib.bootstrap4_utilities.cms_plugins import Bootstrap4SpacingPlugin


plugin_pool.unregister_plugin(Bootstrap4LinkPlugin)


@plugin_pool.register_plugin
class Bootstrap4LinkPlugin(Bootstrap4LinkPlugin):
    name = "Link/Button [deprecated - don't use]"
    text_enabled = False


plugin_pool.unregister_plugin(Bootstrap4PicturePlugin)


@plugin_pool.register_plugin
class Bootstrap4PicturePlugin(Bootstrap4PicturePlugin):
    name = "Picture/Image [deprecated - don't use]"


plugin_pool.unregister_plugin(Bootstrap4SpacingPlugin)


@plugin_pool.register_plugin
class Bootstrap4SpacingPlugin(Bootstrap4SpacingPlugin):
    name = "Spacing [deprecated - don't use]"
