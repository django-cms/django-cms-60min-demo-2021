import logging

from django.apps import AppConfig
from django.conf import settings


logger = logging.getLogger(__name__)


class NavBarAppConfig(AppConfig):
    name = 'backend.plugins.nav_bar'

    def ready(self):
        self._configure_default_navbar_size()

    def _configure_default_navbar_size(self):
        try:
            from backend.site_config.models import SiteConfig
            from backend.plugins.nav_bar.models import NavBarType
    
            site_config = SiteConfig.get_solo()
            if site_config.navbar_default == NavBarType.SMALL:
                settings.CMS_PLACEHOLDER_CONF['header']['default_plugins'][0]['values']['is_full_width'] = False
        except Exception:
            logger.error("Navbar configuration failed", exc_info=True)
