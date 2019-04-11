from utilities.selenium import SeleniumTestCase


class ArchivesTestCase(SeleniumTestCase):
    def test_index(self):
        """ Test that the index page renders correctly """
        self.driver.get(self.live_server_url)
        self.assertIn('Home Page', self.driver.title)
        self.check_log_for_errors()

    def test_browse(self):
        """ Test that archives/browse renders correctly """
        self.driver.get(self.live_server_url + '/archives/browse/')
        self.check_log_for_errors()
