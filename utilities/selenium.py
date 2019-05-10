from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class SeleniumTestCase(StaticLiveServerTestCase):
    def setUp(self):
        """ Sets up our test case before running any tests """
        desires = DesiredCapabilities.CHROME
        desires['loggingPrefs'] = {'browser': 'ALL', 'performance': 'ALL'}

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        self.driver = webdriver.Chrome(desired_capabilities=desires,
                                       chrome_options=options)
        super().setUp()

    def tearDown(self):
        """ Runs after all of our tests run """
        self.driver.quit()
        super().tearDown()

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

    def scroll_to(self, dom_element):
        """
        Scroll to a particular dom_element until it is in view.
        """
        self.driver.execute_script('arguments[0].scrollIntoView(true);', dom_element)
