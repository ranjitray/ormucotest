
import selenium
from selenium import webdriver
import HtmlTestRunner
import unittest
from datetime import  datetime
from OrmucoTest.Page.LoginPage import LoginPage
import time
import logging
from OrmucoTest.Base.Base import BaseClass

from OrmucoTest.Utils import Utils
import time
# import pytest

logging.basicConfig(filename=Utils.get_project_path()+'\\Result\\'+ "Result.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

dt_string= str(time.ctime()).replace(" ","")
error_msg = {"invalid_password": "The user or password is incorrect.",
             "invalid_user": "The user or password is incorrect."
             }

class BaseLoginTest(BaseClass):

    # @pytest.mark.invalidloginMessage

    def test_01_login_invalid_password(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_UserName(Utils.get_properties("uat", "uat_uname"))
        login.enter_Password(Utils.get_properties("invalid_login_data", "invalid_pwd"))
        login.click_SignIn()
        time.sleep(5)
        driver.get_screenshot_as_file(Utils.get_project_path() + '\\ScreenShot\\' + "InvalidPassword.png")

        u = driver.find_element_by_xpath("//span[@class='error']")
        act_err_msg = u.get_attribute('innerText')
        print("Actual Error message: ", act_err_msg)
        self.assertEqual(act_err_msg, error_msg['invalid_password'], "Wrong message displays for invalid password")

    # @pytest.mark.invalidloginMessage
    def test_02_login_invalid_user(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_UserName(Utils.get_properties("uat", "uat_uname"))
        login.enter_Password(Utils.get_properties("invalid_login_data", "invalid_pwd"))
        time.sleep(5)
        login.click_SignIn()

        driver.get_screenshot_as_file(Utils.get_project_path() + '\\Screenshot\\' + "InvalidUserName.png")

        u = driver.find_element_by_xpath("//span[@class='error']")
        act_err_msg = u.get_attribute('innerText')
        print("Actual Error message: ", act_err_msg)
        self.assertEqual(act_err_msg, error_msg['invalid_user'], "Wrong message displays for invalid UserName")

if __name__ == '__main__':
    # unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=Utils.get_project_path() + '\\Reports\\'))

