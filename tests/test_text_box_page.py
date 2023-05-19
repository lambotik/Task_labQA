import allure

from pages.text_box_page import TextBoxPage

@allure.epic('Test Text Box Page')
class TestTextBoxPage:
    class TestTextBox:
        @allure.step('Check Text Box')
        @allure.description('Test input and output data')
        def test_input_and_output_data(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address, output_name,\
                output_email, output_current_addr, output_permanent_address \
                = text_box_page.comparison_of_input_and_output_data()
            assert full_name == output_name, "The full name does not match"
            assert email == output_email, "The email does not match"
            assert current_address == output_current_addr, "The current address does not match"
            assert permanent_address == output_permanent_address, "The permanent address does not match"
