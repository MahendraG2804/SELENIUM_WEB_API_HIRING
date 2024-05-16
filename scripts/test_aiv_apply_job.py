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
    
def test_post_job(driver):
    scholar_login(driver, "mahendraqa@getnada.com", "mahendraqa@getnada.coM")
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//img[@alt='headerIcon']")))  
    click_element(driver, A_link_hire)
    click_element(driver, A_jobcard)
    click_element(driver, A_btn_job_apply)
    enter_text_in_element(driver, A_input_work_experience, "2")
    enter_text_in_element(driver, A_input_notice_period, "3")
    click_element(driver, A_ctc_option)
    click_element(driver, A_select_ctc)
    click_element(driver, A_wfh_hybrid)
    click_element(driver, A_relocate)
    # click_element(driver, A_btn_submit)
    click_element(driver, A_btn_cancel)
    click_element(driver, A_btn_back_jobboard)
    click_element(driver, A_btn_job_applied)
    
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, A_applied_jobcard)))  
    # click_element(driver, A_applied_jobcard)
    # click_element(driver, A_btn_back_jobboard)
    # time.sleep(5)