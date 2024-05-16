from library.basic_selenium_actions import *
from Constants.xpath.topgrephire import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time 
import pytest 
from .login_actions import login

@pytest.fixture(scope="module")
def driver():
    driver = open_browser("https://qa-hiring.topgrep.com")
    yield driver
    driver.quit()       
    
def test_post_job(driver):
    # Fetch login credentials from Excel sheet
    path = "C:/Users/User/OneDrive/Desktop/Hiring_Selenium/TestData/Hiring_test_data.xlsx"
    email = readData(path, "Sheet2", 2, 1)
    password = readData(path, "Sheet2", 2, 2)
    
    # Perform login using fetched credentials
    login(driver, email, password)
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="postBtn"]')))  
    
    rows = getRowCount(path, 'Sheet3')
    for r in range(2, 5):
        # Fetch job details from Excel sheet
        job_title = readData(path, "Sheet3", r, 1)
        job_desc = readData(path, "Sheet3", r, 2)
        job_loc = readData(path, "Sheet3", r, 6)
        # job_emp_type = readData(path, "Sheet3", r, 5)
        job_qualify = readData(path, "Sheet3", r, 3)
        job_responsble = readData(path, "Sheet3", r, 4)
        job_skill = readData(path, "Sheet3", r, 7)
        
        click_element(driver, btn_add_jobs)
        enter_text_in_element(driver, txt_box_job_title, job_title)
        enter_text_in_element(driver, txt_box_job_desc, job_desc)
        enter_text_in_element(driver, txt_box_job_loc, job_loc)
        
        EMP_Type = driver.find_element(By.XPATH, "//div[@id='empType']")
        type_emp =readData(path, "Sheet3", r, 5)
        EMP_Type.send_keys(type_emp)
                        
        # click_element(driver, drop_down_clk_emp_type)
        # click_element(driver, drop_down_emp_type_contract)
        
        enter_text_in_element(driver, txt_box_job_qualify, job_qualify)
        enter_text_in_element(driver, txt_box_job_responsble, job_responsble)
        enter_text_in_element(driver, select_skills, job_skill)
        driver.find_element(By.XPATH, select_skills).send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.XPATH, select_skills).send_keys(Keys.ENTER)
        
        click_element(driver, btn_create_posting)
        time.sleep(2)
        assert wait_until_element_is_visible(driver, Close_job_post_alert), "Job posting alert is not displayed"
        click_element(driver, Close_job_post_alert)
        time.sleep(2)
        assert wait_until_element_is_visible(driver, btn_posted_job), "Job is not posted successfully"
        click_element(driver, btn_posted_job)
        # try:
        #     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, btn_posted_job)))
        #     click_element(driver, btn_posted_job)
        # except TimeoutException:
        #     print("btn_posted_job not found")
       
       
       
# def test_post_job(driver):
#     login(driver, "hiring_robot_auto_test@getnada.com", "hiring_robot_auto_test@getnada.coM")    
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="postBtn"]')))  
#     click_element(driver, btn_add_jobs)
#     enter_text_in_element(driver, txt_box_job_title, "Multi Tasker Admin Role")
#     enter_text_in_element(driver, txt_box_job_desc, "We are an Australian Group dealing in manufacturing/Importing of Sporting Goods, Customised Sublimation Sports/Fashion Wear & Fabrics , Selling Van Car Accessories & Installations at our factory in Moorabbin 3189 Our partner is also a psychic medium.")
#     enter_text_in_element(driver, txt_box_job_loc, "PUNE")
#     click_element(driver, drop_down_clk_emp_type)
#     click_element(driver, drop_down_emp_type_contract)
#     enter_text_in_element(driver, txt_box_job_qualify, "ANY DEGREE With Age below 50")
#     enter_text_in_element(driver, txt_box_job_responsble, "We seek to employ a young highly dynamic and self-motivated multi tasker person who can bring the following to the business")
#     enter_text_id_element(By.XPATH, select_skills).send_keys(Keys.PAGE_DOWN)
#     # driver.find_element_by_name("Value").send_keys(Keys.ENTER)
#     driver.find_element(By.XPATH, select_skills).send_keys(Keys.ENTER)
#     click_element(driver, btn_create_posting)
#     time.sleep(5)n_element(driver, select_skills, "selenium")
#     driver.find