from typing import List

from cms.models import Page
from django.core.management import call_command
from django.test import Client
from django.test import RequestFactory
from django.test import TestCase
from django.contrib import admin
from django.urls import reverse
from django.apps import apps

from backend.auth.models import User


class PagesTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        user = User.objects.create_superuser(email='test+test@what.digital', password='test')
        cls.client = Client()
        cls.client.force_login(user)

        factory = RequestFactory()
        request = factory.get('/')
        request.user = user
        request.session = {}
        cls.request = request

        call_command('migrate')

    def test_admin_pages(self):
        error_list: List[str] = []
        for model_config_dict in admin.site.get_app_list(self.request):
            app_label: str = model_config_dict['app_label']
            for model_dict in model_config_dict['models']:
                model_name: str = model_dict['object_name']
                model_first_instance = apps.get_model(app_label, model_name)
                if model_first_instance:
                    change_url = reverse(
                        f'admin:{app_label}_{model_name.lower()}_change',
                        args=[model_first_instance.pk],
                    )
                    self._check_and_collect_errors(change_url, error_list)
                    
                list_url = reverse(f'admin:{app_label}_{model_name.lower()}_changelist')
                self._check_and_collect_errors(list_url, error_list)

                add_url = reverse(f'admin:{app_label}_{model_name.lower()}_add')
                self._check_and_collect_errors(add_url, error_list)
        for error in error_list:
            print(error)
        if error_list:
            self.fail(f"{len(error_list)} urls failed.")

    def test_published_pages(self):
        error_list: List[str] = []
        for page_published in Page.objects.filter(publisher_is_draft=False):
            url = page_published.get_absolute_url()
            self._check_and_collect_errors(url, error_list)
        for error in error_list:
            print(error)
        if error_list:
            self.fail(f"{len(error_list)} urls failed.")

    def _check_and_collect_errors(self, url: str, error_list: List[str]):
        response = self.client.get(url)
        is_error = response.status_code >= 500
        if is_error:
            error_list.append(f'{response.status_code} - {url}')
