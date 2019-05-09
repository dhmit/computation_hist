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

    def test_stories(self):
        """ Test that archives/stories render correctly """
        self.driver.get(self.live_server_url + '/archives/stories/')
        self.check_log_for_errors()

    def test_search_without_input(self):
        """ Test that the advanced/document search renders correctly with no input """
        self.driver.get(self.live_server_url + '/archives/search/')
        self.check_log_for_errors()

    def test_search(self):
        """ Test that the search bar works correctly"""
        self.driver.get(self.live_server_url)
        # chromedriver defaults to a collapsed display, hence needing to click the toggler
        self.driver.find_element_by_class_name('navbar-toggler').click()
        self.driver.implicitly_wait(5)
        search = self.driver.find_element_by_id('basic_search')
        search.clear()
        search.send_keys('test')
        self.driver.find_element_by_id('basic_search_submit_button').click()
        self.check_log_for_errors()

    def test_search_with_keyword(self):
        """ Test that the search is accessible through basic search """
        self.driver.get(self.live_server_url + '/archives/search/?keyword=test')
        self.check_log_for_errors()

    def test_a_story(self):
        """ Test that a story on the index page can be loaded without issue"""
        self.driver.get(self.live_server_url)
        self.assertIn('Home Page', self.driver.title)
        story = self.driver.find_elements_by_class_name("story-teaser-img-container")[0]
        story.find_element_by_xpath('..').click()
        self.check_log_for_errors()


