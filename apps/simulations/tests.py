from utilities.selenium import SeleniumTestCase


class SimulationsTestCase(SeleniumTestCase):

    def test_simulations(self):
        """ Test that the standard search renders correctly with no input """
        self.driver.get(self.live_server_url + '/simulations/')
        self.check_log_for_errors()

    def test_assembly_addition(self):
        """ Test that assembly addition simulations works and that the buttons function """
        self.driver.find_element_by_class_name('introjs-skipbutton').click()
        self.driver.get(self.live_server_url + '/simulations/assembly_addition/')
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('step_button').click()  # test the step button
        self.driver.find_element_by_id('reset_button').click()  # test the reset button
        self.driver.find_element_by_id('run_button').click()  # test the run button
        self.check_log_for_errors()

    def test_floating_point_operations(self):
        """ Test that the floating point operation works and that the buttons function """
        self.driver.find_element_by_class_name('introjs-skipbutton').click()
        self.driver.get(self.live_server_url + '/simulations/floating_point_operations/')
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('step_button').click()  # test the step button
        self.driver.find_element_by_id('reset_button').click()  # test the reset button
        self.driver.find_element_by_id('run_button').click()  # test the run button
        self.check_log_for_errors()

    def test_looping_with_tix(self):
        """ Test that the looping with tix works and that the buttons function """
        self.driver.find_element_by_class_name('introjs-skipbutton').click()
        self.driver.get(self.live_server_url + '/simulations/looping_with_tix/')
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('step_button').click()  # test the step button
        self.driver.find_element_by_id('reset_button').click()  # test the reset button
        self.driver.find_element_by_id('run_button').click()  # test the run button
        self.check_log_for_errors()

    def test_general_assembler(self):
        """ Test that the general assembler works and that the buttons function """
        self.driver.find_element_by_class_name('introjs-skipbutton').click()
        self.driver.get(self.live_server_url + '/simulations/general_assembler')
        self.driver.find_element_by_id('add_line').click()  # test adding line
        self.driver.find_element_by_id('remove_line').click()  # test removing line
        # fill in code boxes
        self.driver.find_element_by_class_name('code_label').send_keys("LABEL")
        self.driver.find_element_by_class_name('code_operation').send_keys("ADD")
        self.driver.find_element_by_class_name('code_numbers').send_keys("LABEL+1, 3")
        self.driver.find_element_by_id('assemble_button').click()  # assemble code
        self.driver.find_element_by_id('step_button').click()  # test the step button
        self.driver.find_element_by_id('run_button').click()  # test the run button
        self.driver.find_element_by_id('highlight_button').click()  # test the highlight toggle
        self.driver.find_element_by_id('clear_button').click()  # test the clear button
        self.check_log_for_errors()
