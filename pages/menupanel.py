from pages.login import *


class User_Menu:
    def __init__(self, driver):
        self.driver = driver
        self.search_locator = '//*[@id="gatsby-focus-wrapper"]/div/header/div/button/svg/path'
        self.LogOut_locator = '//*[@id="gatsby-focus-wrapper"]/div/header/div/div[4]'
        self.login_locator = Login.login_button_class


    def search_page(self, time=5):
        self.driver.find_element(By.XPATH, self.search_locator).click()
        return WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.LogOut_locator)),
            message=f"Menu {self.search_locator} has not been opened")

    def LogOut(self, time=10):
        self.driver.find_element(By.XPATH, self.LogOut_locator).click()
        return WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.login_locator)),
            message=f"Failed to logout via {self.login_locator}")
