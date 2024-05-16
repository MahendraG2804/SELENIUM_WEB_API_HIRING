from library.basic_selenium_actions import *
from library.comparison_actions import *
from Constants.xpath.art_of_testing import *
from library.exeception_handlers import *
from Constants.xpath.saucedemo import *

# from basic_functions import *
import time 
import pytest

@pytest.fixture
def driver():
    driver = open_browser("https://www.saucedemo.com/")
    yield driver
    # Teardown driver
    driver.quit()
    
    
# Testing login in successful
def test_login(driver):
    wait_until_element_is_visible(driver, txt_box_username)
    enter_text_in_element(driver, txt_box_username, 'standard_user')
    enter_text_in_element(driver, txt_box_password, 'secret_sauce')
    click_element(driver, btn_login)
    wait_until_element_is_visible(driver, "//span[contains(text(), 'Products')]")
    should_be_equal_as_strings(driver, "//span[contains(text(), 'Products')]", "Products")
    
# Product is found successfully
def test_product_search(driver):
    pass

# Add to cart button is working or not
def test_add_to_cart(driver):
    pass
    
# Check if product is added to cart
def test_cart_functionality(driver):
    pass

# Checkout
def test_checkout(driver):
    pass
