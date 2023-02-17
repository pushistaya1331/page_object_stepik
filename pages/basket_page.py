from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def check_product_not_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Product in basket is presented, but should not be"
        
    def check_message_for_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MSG), \
            "Message for empty basket is not presented"
