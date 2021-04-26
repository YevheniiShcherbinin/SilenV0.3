from pages.login import *
from pages.usermenu import *
from pages.change_email import *
from pages.editingProfile import *
from pages.headernavigation import *
from selenium import webdriver


class Test:

    def test_koralgo_dev(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://dev.koralgo.com/")

        login = Login(driver)
        login.login()
        login.enter_credentials()
        login.login_to_app()

        user_nav_menu = User_Menu(driver)
        user_nav_menu.menu_button_click()
        user_nav_menu.settings_tab()

        update_email = email_changing(driver)
        update_email.enter_new_values()
        update_email.click_confirm()

        user_nav_menu.profile_info_tab()

        update_user_info = profile_info_updating(driver)
        update_user_info.clear_old_values()
        update_user_info.add_new_values()
        update_user_info.save_added_changes()

        topnavigation = head_navigation(driver)
        topnavigation.mainpage()
        topnavigation.search()
        topnavigation.Log_out()

        driver.quit()


if __name__ == "__main__":
    Test.test_koralgo_dev(self=Test())
