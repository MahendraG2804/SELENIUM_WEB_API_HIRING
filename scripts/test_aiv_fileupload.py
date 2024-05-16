from library.basic_selenium_actions import *
from Constants.xpath.topgrephire import *
from Constants.xpath.aivagam import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import pytest
from .login_actions import scholar_login

@pytest.fixture(scope="module")
def driver():
    driver = open_browser("https://qa-portal.topgrep.com")
    yield driver
    driver.quit()
        
    
def test_fileupload_job(driver):
    scholar_login(driver, "mahendraqa@getnada.com", "mahendraqa@getnada.coM")
    time.sleep(3)
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//img[@alt='headerIcon']")))  
    click_element(driver, A_link_hire)
    time.sleep(3)
    click_element(driver, A_btn_view_profile)
    time.sleep(3)
    click_element(driver, A_btn_edit_profile)
    time.sleep(3)
    Fileupload = driver.find_element(By.XPATH, A_drop_file)
    Fileupload.send_keys("E:/TOPGREP/Certifications/dp.png")
    
    time.sleep(3)       
    click_element(driver, A_btn_update)
    time.sleep(3)
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, A_applied_jobcard)))  
    # click_element(driver, A_applied_jobcard)
    # click_element(driver, A_btn_back_jobboard)
    # time.sleep(5)