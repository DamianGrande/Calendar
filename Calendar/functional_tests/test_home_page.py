import unittest

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class HomePageTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.close()

    def test_correct_title_on_title_tag(self):
        self.browser.get(self.live_server_url)

        self.assertEqual('Calendar', self.browser.title)

    def test_main_div_present(self):
        self.browser.get(self.live_server_url)

        self.assertTrue(self.browser.find_element_by_id('app'))

    if __name__ == '__main__':
        unittest.main()
