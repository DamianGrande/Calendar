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

    def test_correct_structure(self):
        self.browser.get(self.live_server_url)

        app = self.browser.find_element_by_id('app')
        week = app.find_element_by_id('calendar-week')
        entry = app.find_element_by_id('calendar-entry')
        days = week.find_elements_by_xpath("//*[starts-with(@id, 'day')]")

        self.assertEqual(7, len(days))
        self.assertTrue(len(days[0].find_elements_by_xpath("//*[starts-with(@id, 'event')]")) > 0)

        if __name__ == '__main__':
            unittest.main()
