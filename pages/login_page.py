from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "/login" in current_url, "Wrong login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_input.send_keys(email)
        password_input1 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIRST)
        password_input1.send_keys(password)
        password_input2 = self.browser.find_element(*LoginPageLocators.PASSWORD_SECOND)
        password_input2.send_keys(password)
        reg_btn = self.browser.find_element(*LoginPageLocators.REG_BTN)
        reg_btn.click()
