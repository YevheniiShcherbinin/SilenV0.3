from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class head_navigation:

    def __init__(self, driver):
        self.driver = driver
        self.main_page_locator = '/html/body/div[1]/div[1]/header/div/div[1]/a'
        self.main_page_element = '/html/body/div[1]/div[1]/div/main/div[2]/div/div[1]/div[1]/div[1]'
        self.search_button_locator = '/html/body/div[1]/div[1]/div/header/div/button'
        self.search_page_element = '/html/body/div[1]/div[1]/div/main/div[1]/div/div/div[2]/div'
        self.Log_out_button_locator = '/html/body/div[1]/div[1]/div/header/div/div[4]'
        self.login_locator = 't-500'

    def mainpage(self, time=100):
        self.driver.find_element(By.XPATH, self.main_page_locator).click()
        return WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.main_page_element)),
            message=f"Main page {self.main_page_element} has not been opened")

    def search(self, time=100):
        self.driver.find_element(By.XPATH, self.search_button_locator).click()
        return WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.search_page_element)),
            message=f"Search page {self.search_page_element} has not been opened")

    def Log_out(self, time=100):
        self.driver.find_element(By.XPATH, self.Log_out_button_locator).click()
        return WebDriverWait(self.driver, time).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, self.login_locator)),
            message=f"Failed to logout via {self.login_locator}")
