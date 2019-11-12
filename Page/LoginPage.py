from selenium import webdriver
import selenium

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.username ="username"
        self.password = "password"
        self.signIn_button ="//button[contains(text(),'CONNEXION')]"
        self.invalidPassword_error_msg = "//span[@class='error']"
        self.languageMenu_selector = "//div[@class='lang_menu d-table centered_object dropdown_trigger hover']"
        self.Select_lang = "//td[contains(text(),'English')]"

    def select_language_menu(self):
        self.driver.find_element_by_xpath(self.languageMenu_selector)

    def enter_UserName(self, username):
        self.driver.find_element_by_id(self.username).clear()
        self.driver.find_element_by_id(self.username).send_keys(username)

    def enter_Password(self, password):
        self.driver.find_element_by_id(self.password).clear()
        self.driver.find_element_by_id(self.password).send_keys(password)

    def click_SignIn(self):
        self.driver.find_element_by_xpath(self.signIn_button).click()

    def get_invalid_errorMsg(self, element):
        msg = element.get_attribute('innerText')
        # msg = self.driver.find_element_by_xpath(self.invalidPassword_error_msg).text
        return msg












