from functional_tests.base import FunctionalTest
__author__ = 'lee'
from selenium import webdriver


class MainSiteVisitorTest(FunctionalTest):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_user_get_main_site(self):
        # User heard about new cool site
        # to manage his course, so he goes to
        # the website
        self.browser.get(self.live_server_url)

        # He see that main site is named Nauczka
        assert 'Nauczka' in self.browser.title

