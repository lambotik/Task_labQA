import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(5)

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url: ' + get_url)

    def open(self):
        with allure.step(f'Open page: {self.url}'):
            self.driver.get(self.url)

    @allure.step('Check element is visible')
    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Check elements are visible')
    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Check element is present')
    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Check elements are present')
    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def go_to_element(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Check elements is clickable')
    def elements_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Remove footer')
    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        print('\nRemove Footer')


    @allure.step('Remove fixedban')
    def remove_fixedban(self):
        """"This method removes the advertising banner"""
        self.driver.execute_script("document.getElementById('fixedban').style.display = 'none'")
        print('Remove Fixedban')

    @allure.step('Attach screenshot')
    def attach_screenshot(self, element):
        """Create screenshot of current window and attach it in allure report"""
        element_name = ''.join(element)
        allure.attach(self.driver.get_screenshot_as_png(), name=element_name, attachment_type=AttachmentType.PNG)
