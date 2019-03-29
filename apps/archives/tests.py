import json

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait

from django.test import TestCase, LiveServerTestCase

# TODO(ra): generalize some of this test code

class ArchivesTestCase(LiveServerTestCase):
    def setUp(self):
        desires = DesiredCapabilities.CHROME
        desires['loggingPrefs'] = {'browser': 'ALL', 'performance': 'ALL'}
        self.driver = webdriver.Chrome(desired_capabilities=desires)
        self.server = 'http://localhost:8000/'

        super(ArchivesTestCase, self).setUp()

    def tearDown(self):
        self.driver.quit()
        super(ArchivesTestCase, self).tearDown()

    def test_index(self):
        self.driver.get(self.server)
        self.check_response_status()
        self.check_log_for_errors()

    def test_browse(self):
        self.driver.get(self.server + 'archives/browsenope/')
        self.check_response_status()
        self.check_log_for_errors()

    def check_response_status(self):
        performance_log = self.driver.get_log('performance')

        response_status = 0
        for plog in performance_log:
            if 'message' not in plog:
                continue # should not happen...
            msg_args = json.loads(plog['message'])
            if 'message' not in msg_args:
                continue
            msg_args_msg = msg_args['message']
            if 'method' not in msg_args_msg:
                continue
            if msg_args_msg['method'] != 'Network.responseReceived':
                continue
            params = msg_args_msg['params']
            if 'response' not in params:
                continue
            response = params['response']
            if 'status' not in response:
                continue
            response_status = response['status']
            # continue to get last status...
            print(response_status)

        okay_statuses = (200, 304)
        self.assertIn(response_status, okay_statuses,
                    f'Status of {response_status} is not in {okay_statuses}')


    def check_log_for_errors(self):
        self.driver.execute_script("console.log('Nothing to see here – move along.');")
        log = self.driver.get_log('browser')
        error_messages = []
        print('log: ', log)

        for this_log in log:
            if (this_log['level'] == 'SEVERE'):
                error_messages.append(this_log['message'])

        if error_messages:
            all_msgs = "\n".join(error_messages)
            self.fail(f'Errors found on page: \n {all_msgs}')
