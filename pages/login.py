from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Login:
    login_button_class = 't-500'

    def __init__(self, driver):
        self.driver = driver
        self.sign_in_button_class = "t-500"
        self.email = "yevhenii.shcherbinin.cr+21@gmail.com"
        self.password = "Pass1234"
        self.username_locator = "email"
        self.password_locator = "password"
        self.login_button_selector = '.btn.btn_block.btn-uppercased.btn_common.btn_auth.t-600'
        self.sign_in_form_selector = ".auth-wrapper.container-bordered"
        self.navigation_locator = "search-page-module--input--3ty5S"

    def login(self, time=100):
        self.driver.find_element(By.CLASS_NAME, self.login_button_class).click()
        return WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.sign_in_form_selector)),
            message=f"Login page {self.sign_in_form_selector} has not been opened")

    def enter_credentials(self):
        self.driver.find_element(By.NAME, self.username_locator).send_keys(self.email)
        self.driver.find_element(By.NAME, self.password_locator).send_keys(self.password)

    def login_to_app(self, time=100):
        self.driver.find_element(By.CSS_SELECTOR, self.login_button_selector).click()
        return WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, self.navigation_locator)),
            message=f"Failed to login, navigation bar {self.navigation_locator} not found")

