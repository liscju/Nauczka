from django.contrib.staticfiles.testing import StaticLiveServerTestCase

__author__ = 'lee'

from selenium import webdriver


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()











