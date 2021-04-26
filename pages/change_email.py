from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class email_changing:

    def __init__(self, driver):
        self.driver = driver
        self.email = "yevhenii.shcherbinin.cr+21@gmail.com"
        self.password = "Pass1234"
        self.password_locator = '//*[@id="gatsby-focus-wrapper"]/main/div/div/div[2]/div[2]/div/form/div[2]/div[' \
                                '2]/div[2]/input '
        self.new_email_locator = '/html/body/div[1]/div[1]/main/div/div/div[2]/div[2]/div/form/div[2]/div[3]/div[' \
                                 '2]/input '
        self.confirm_locator = '/html/body/div[1]/div[1]/main/div/div/div[2]/div[2]/div/form/div[2]/button/span'
        self.updated_email_modal_locator = '/html/body/div[1]/div[1]/main/div/div/div[2]/div[2]/div/form/div[1]'

    def enter_new_values(self):
        self.driver.find_element(By.XPATH, self.password_locator).send_keys(self.password)
        self.driver.find_element(By.XPATH, self.new_email_locator).send_keys(self.email)

    def click_confirm(self, time=100):
        self.driver.find_element(By.XPATH, self.confirm_locator).click()
        return WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.updated_email_modal_locator)),
            message=f"Confirm modal {self.updated_email_modal_locator} not found")
