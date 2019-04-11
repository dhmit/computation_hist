from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from django.contrib.staticfiles.testing import StaticLiveServerTestCase


# TODO(ra): generalize some of this test code
class ArchivesTestCase(StaticLiveServerTestCase):
    def setUp(self):
        desires = DesiredCapabilities.CHROME
        desires['loggingPrefs'] = {'browser': 'ALL', 'performance': 'ALL'}

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        self.driver = webdriver.Chrome(desired_capabilities=desires,
                                       chrome_options=options)
        super(ArchivesTestCase, self).setUp()

    def tearDown(self):
        self.driver.quit()
        super(ArchivesTestCase, self).tearDown()

    def test_index(self):
        self.driver.get(self.live_server_url)
        self.assertIn('Home Page', self.driver.title)
        self.check_log_for_errors()

    def test_browse(self):
        self.driver.get(self.live_server_url + '/archives/browse/')
        self.check_log_for_errors()

    def check_log_for_errors(self):
        """ Check the console log for any errors. Fail if we find any. """
        log = self.driver.get_log('browser')
        error_messages = []

        for this_log in log:
            if this_log['level'] == 'SEVERE':
                error_messages.append(this_log['message'])

        if error_messages:
            all_msgs = "\n".join(error_messages)
            self.fail(f'Errors found on page: \n {all_msgs}')

