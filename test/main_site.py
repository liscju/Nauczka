__author__ = 'lee'

from selenium import webdriver
import unittest

class MainSiteVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_user_get_main_site(self):
        # User heard about new cool site
        # to manage his course, so he goes to
        # the website
        self.browser.get('http://localhost:5000')

        # He see that main site is named Nauczka
        assert 'Nauczka' in self.browser.title

if __name__ == '__main__':
    unittest.main(warnings='ignore')
