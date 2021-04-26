from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class User_Menu:

    #account_profile_locator = '//*[@id="gatsby-focus-wrapper"]/header/div/div[2]/div[2]/a[1]'
    #bookings_locator = '//*[@id="gatsby-focus-wrapper"]/header/div/div[2]/div[2]/a[2]'
    #settings_locator = '//*[@id="gatsby-focus-wrapper"]/header/div/div[2]/div[2]/a[3]'

    #account_profile_locator_url = "https://dev.koralgo.com/customers/search-profile"
    #bookings_locator_url = "https://dev.koralgo.com/customers/bookings"
    #settings_url = "https://dev.koralgo.com/customers/settings/email"

    def __init__(self, driver):
        self.driver = driver
        self.menu_button_locator = "Mask"
        self.menu_form_locator = "btn.flex.flex-v-center.ClientMenu-module--close--1wT_u"
        self.menu_settings_locator = '/html/body/div[1]/div[1]/div/header/div/div[2]/div[2]/a[3]'
        self.setting_menu_form = '/html/body/div[1]/div[1]/main/div/div/div[2]/div[1]/div'
        self.profile_info_form_locator = '/html/body/div[1]/div[1]/main/div/div/div[2]/div[1]/div/a[3]'
        self.profile_info_modal_locator = '/html/body/div[1]/div[1]/main/div/div/div[2]/div[2]/div/form/div[1]'


    def menu_button_click(self, time=100):
        self.driver.find_element(By.ID, self.menu_button_locator).click()
        return WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, self.menu_form_locator)),
            message=f"Failed,menu form {self.menu_form_locator} not found")

    def settings_tab(self, time=100):
        self.driver.find_element(By.XPATH, self.menu_settings_locator).click()
        return WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.setting_menu_form)),
            message=f"Failed,menu form {self.setting_menu_form} not found")

    def profile_info_tab(self, time=100):
        self.driver.find_element(By.XPATH, self.profile_info_form_locator).click()
        return WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.profile_info_modal_locator)),
            message=f"Failed,change info form {self.profile_info_modal_locator} not found")
