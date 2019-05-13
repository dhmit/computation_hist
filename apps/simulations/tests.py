from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utilities.selenium import SeleniumTestCase


class SimulationsTestCase(SeleniumTestCase):

    def test_simulations(self):
        """ Test that the standard search renders correctly with no input """
        self.driver.get(self.live_server_url + '/simulations/')
        self.check_log_for_errors()

    def skip_intro_js(self):
        """ Skipping intro_js is a tricky business, as it only appears
            the first time through one of the demos... which is why we
            have this try/except pattern here. """

        wait = WebDriverWait(self.driver, 2)
        try:
            el = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'introjs-skipbutton')))
        except TimeoutException:
            # introjs already ran on a different demo, so it won't show up
            return

        el.click()
        overlay = self.driver.find_element_by_class_name('introjs-overlay')
        wait.until(EC.staleness_of(overlay))

    def test_simulation_demos(self):
        """ Test that the simulation demos work and that the buttons function """
        demos = ['floating_point_operations',
                 'assembly_addition',
                 'looping_with_tix']
        for i, demo in enumerate(demos):
            self.driver.get(self.live_server_url + '/simulations/' + demo)
            self.skip_intro_js()
            self.driver.find_element_by_id('step_button').click()  # test the step button
            self.driver.find_element_by_id('reset_button').click()  # test the reset button
            self.driver.find_element_by_id('run_button').click()  # test the run button
            self.check_log_for_errors()

    def test_general_assembler(self):
        """ Test that the general assembler works and that the buttons function """
        self.driver.get(self.live_server_url + '/simulations/general_assembler')

        self.skip_intro_js()

        self.driver.find_element_by_id('add_line').click()  # test adding line
        self.driver.find_element_by_id('remove_line').click()  # test removing line

        # fill in code boxes
        self.driver.find_element_by_class_name('code_label').send_keys("LABEL")
        self.driver.find_element_by_class_name('code_operation').send_keys("ADD")
        self.driver.find_element_by_class_name('code_numbers').send_keys("LABEL+1, 3")
        self.scroll_to(self.driver.find_element_by_id('assemble_button'))
        self.driver.find_element_by_id('assemble_button').click()  # assemble code
        self.driver.find_element_by_id('step_button').click()  # test the step button
        self.driver.find_element_by_id('run_button').click()  # test the run button
        self.driver.find_element_by_id('highlight_button').click()  # test the highlight toggle
        self.driver.find_element_by_id('clear_button').click()  # test the clear button
        self.check_log_for_errors()
