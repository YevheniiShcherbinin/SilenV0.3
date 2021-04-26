from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class profile_info_updating:
    def __init__(self, driver):
        self.driver = driver
        self.nickname_locator = '/html/body/div[1]/div[1]/main/div/div/div[2]/div[2]/div/form/div[2]/div[1]/div[2]/input'
        self.first_name_locator = '/html/body/div[1]/div[1]/main/div/div/div[2]/div[2]/div/form/div[2]/div[3]/div[2]/input'
        self.last_name_locator = '/html/body/div[1]/div[1]/main/div/div/div[2]/div[2]/div/form/div[2]/div[4]/div[2]/input'
        self.nickname = "Test User"
        self.first_name = "John"
        self.last_name = "Doe"
        self.save_changes = '/html/body/div[1]/div[1]/main/div/div/div[2]/div[2]/div/form/div[3]/button'
        self.changes_info_locator = '/html/body/div[1]/div[1]/main/div/div/div[2]/div[2]/div/form/div[1]'

    def clear_old_values(self):
        self.driver.find_element(By.XPATH, self.nickname_locator).clear()
        self.driver.find_element(By.XPATH, self.first_name_locator).clear()
        self.driver.find_element(By.XPATH, self.last_name_locator).clear()

    def add_new_values(self):
        self.driver.find_element(By.XPATH, self.nickname_locator).send_keys(self.nickname)
        self.driver.find_element(By.XPATH, self.first_name_locator).send_keys(self.first_name)
        self.driver.find_element(By.XPATH, self.last_name_locator).send_keys(self.last_name)

    def save_added_changes(self, time=100):
        self.driver.find_element(By.XPATH, self.save_changes).click()
        return WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.changes_info_locator)),
            message=f"Failed, changes {self.changes_info_locator} not found")
