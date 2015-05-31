from django.core.urlresolvers import resolve
from django.test import TestCase
from nauczka.home.views import *

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)