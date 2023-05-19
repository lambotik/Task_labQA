import allure

from generator.generator import generated_person
from locators.text_box_page_locators import TextBoxPageLocators
from pages.base_page import BasePage
from utilities.logger import Logger


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    # Actions

    """"Fills the form with random data using the generator and the faker library.
     Returns the data entered in the form"""
    @allure.step("Fill in all fields")
    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        with allure.step('Filing fields'):
            self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
            print(f'Entered Full name: {full_name}')
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            print(f'Entered Email: {email}')
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
            print(f'Entered Current address: {current_address}')
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
            print(f'Entered Permanent address: {permanent_address}')
        with allure.step('Click submit button'):
            self.element_is_visible(self.locators.SUBMIT).click()
            print(f'Pressed button: Submit')
        return full_name, email, current_address, permanent_address

    @allure.step('Check filled form')
    def check_filled_form(self):
        output_full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        output_email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        output_current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        output_permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        print(
            f'Created Full name: {output_full_name}\nCreated Email: {output_email}'
            f'\nCreated Current address: {output_current_address}\nCreated Permanent address: {output_permanent_address}')
        return output_full_name, output_email, output_current_address, output_permanent_address

    # Methods for logger
    def comparison_of_input_and_output_data(self):
        Logger.add_start_step(method='comparison_of_input_and_output_data')
        full_name, email, current_address, permanent_address = self.fill_all_fields()
        Logger.add_step(method='fill_all_fields')
        output_full_name, output_email, output_current_address, output_permanent_address = self.check_filled_form()
        Logger.add_step(method='check_filled_form')
        Logger.add_end_step(url=self.driver.current_url, method='comparison_of_input_and_output_data')
        return full_name, email, current_address, permanent_address, \
            output_full_name, output_email, output_current_address, output_permanent_address
