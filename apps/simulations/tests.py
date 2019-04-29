from utilities.selenium import SeleniumTestCase


class SimulationsTestCase(SeleniumTestCase):

    def test_simulations(self):
        """ Test that the standard search renders correctly with no input """
        self.driver.get(self.live_server_url + '/simulations/')
        self.check_log_for_errors()

    def test_assembly_addition(self):
        """ Test that assembly addition simulations works and that the buttons function """
        self.driver.get(self.live_server_url + '/simulations/assembly_additon/')
        self.driver.find_element_by_id('step_button').click()  # test the step button
        self.driver.find_element_by_id('reset_button').click()  # test the reset button
        self.driver.find_element_by_id('run_button').click()  # test the run button
        self.check_log_for_errors()

    def test_floating_point_operations(self):
        """ Test that the floating point operation works and that the buttons function """
        self.driver.get(self.live_server_url + '/simulations/floating_point_operations/')
        self.driver.find_element_by_id('step_button').click()  # test the step button
        self.driver.find_element_by_id('reset_button').click()  # test the reset button
        self.driver.find_element_by_id('run_button').click()  # test the run button
        self.check_log_for_errors()

    def test_looping_with_tix(self):
        """ Test that the looping with tix works and that the buttons function """
        self.driver.get(self.live_server_url + '/simulations/looping_with_tix/')
        self.driver.find_element_by_id('step_button').click()  # test the step button
        self.driver.find_element_by_id('reset_button').click()  # test the reset button
        self.driver.find_element_by_id('run_button').click()  # test the run button
        self.check_log_for_errors()

    def test_general_assembler(self):
        """ Test that the general assembler works and that the buttons function """
        self.driver.get(self.live_server_url + '/simulations/looping_with_tix/')
        self.driver.find_element_by_id('code_box').send_keys("ADD 5, 1") # fill in code box
        self.driver.find_element_by_id('assemble_button').click()  # assemble code
        self.driver.find_element_by_id('step_button').click()  # test the step button
        self.driver.find_element_by_id('run_button').click()  # test the run button
        self.driver.find_element_by_id('highlight_button').click()  # test the highlight toggle
        self.driver.find_element_by_id('clear_button').click()  # test the clear button
        self.check_log_for_errors()
