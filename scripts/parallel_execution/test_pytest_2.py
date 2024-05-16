import pytest
from .configtest import setup
from selenium.webdriver.common.by import By
from library.basic_selenium_actions import *
from library.data_helper import *
from Constants.xpath.saucedemo import *
import time


@pytest.mark.usefixtures("setup")
class TestExampleTwo:
    def test_login(self, setup):
        driver=setup
        data = read_csv_data("C:/Users/User/OneDrive/Desktop/Selenium_LMS/Constants/data/saucedemo_login.csv") 
        enter_text_in_element(driver, txt_box_username, data[1]['txt_box_username'])
        enter_text_in_element(driver, txt_box_password, data[1]['txt_box_password'])
        click_element(self.driver, btn_login)
        take_screenshot(driver, "locked_out_user.png")