from library.basic_selenium_actions import *
from library.comparison_actions import *
from Constants.xpath.topgrephire import *
from Constants.xpath.aivagam import*
from library.exeception_handlers import *
from library.data_helper import *

from selenium.webdriver.common.keys import Keys
from library.vedio_recorder import recording
# from basic_functions import *
import time 
import pytest

@pytest.fixture(scope="module")
# @pytest.fixture
def driver():
    driver = open_browser("https://qa-portal.topgrep.com")
    yield driver
    # Teardown driver
    driver.quit()
    

def test_login(driver):
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[normalize-space()='AIVAGAM']")))
    click_element(driver, A_btn_signin)
    enter_text_in_element(driver, A_txtbox_email, "mahendraqa@getnada.com")
    time.sleep(1)
    # driver.implicitly_wait(20)
    enter_text_in_element(driver, A_txtbox_password, "mahendraqa@getnada.coM")
    time.sleep(1)
    click_element(driver, A_btn_login)
    time.sleep(1)