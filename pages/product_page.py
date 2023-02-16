from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        bsk_btn = self.browser.find_element(*ProductPageLocators.ADD_BSK_BTN)
        bsk_btn.click()
    
    def should_be_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_NAME), "Message is not presented"

    def check_product_name_in_message(self):
        name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        msg_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert name  == msg_name, "Book isn't in basket"

    def check_product_price_in_message(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        msg_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_PRICE).text
        assert price == msg_price, "Price is wrong"
    