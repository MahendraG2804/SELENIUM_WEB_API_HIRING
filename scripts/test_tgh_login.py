from library import basic_selenium_actions
from library.basic_selenium_actions import *
from library.comparison_actions import *
from Constants.xpath.topgrephire import *
from library.exeception_handlers import *
from library.data_helper import *
import openpyxl

from selenium.common.exceptions import StaleElementReferenceException

from selenium.webdriver.common.keys import Keys
from library.vedio_recorder import recording
import multiprocessing
# from basic_functions import *
import time 
import pytest 

@pytest.fixture(scope="module")
def driver():
    driver = open_browser("https://qa-hiring.topgrep.com")
    yield driver
    # Teardown driver
    driver.quit()



def test_login_from_excel(driver):
    path = "C:/Users/User/OneDrive/Desktop/Hiring_Selenium/TestData/Hiring_test_data.xlsx"
    rows = getRowCount(path, 'Sheet1')
    cols = getColumnCount(path, 'Sheet1')
    click_element(driver, btn_singin)
    time.sleep(1)
    print("ROWS PRESENT:", rows)
    print("COLUMNS PRESENT:", cols)

    print("Starting loop")
    for r in range(2, rows+1):
        email = readData(path, "Sheet1", r, 1)
        password = readData(path, "Sheet1", r, 2)
    
        email_field = driver.find_element(By.XPATH, txt_box_email)
        email_field.send_keys(email)        
        
        password_field = driver.find_element(By.XPATH, txt_box_password)
        password_field.send_keys(password)
                
        click_element(driver, btn_login)

        time.sleep(1)

        try:
            changedURL = "https://qa-hiring.topgrep.com/jobs"
            if driver.current_url == changedURL:
                print("Correct Login Credentials")
                writeData (path, "Sheet1", r, 3, "Correct Login Credentials")
                click_element(driver, "//section[@class='nav-links']//div")
                # password_field.clear()
                # time.sleep(1)
                # email_field.clear()           
            else:
                password_field.clear()
                time.sleep(1)
                email_field.clear()
                print("Incorrect Login Credentials")
                writeData (path, "Sheet1", r, 3, "Incorrect Login Credentials")    
                time.sleep(1)
            
        except StaleElementReferenceException:
            # Retry the action by locating the elements again
            email_field = driver.find_element(By.XPATH, txt_box_email)
            email_field.send_keys(email)        
        
            password_field = driver.find_element(By.XPATH, txt_box_password)
            password_field.send_keys(password)
                
            click_element(driver, btn_login)

            time.sleep(1)
            
            # Handle the outcome after retrying

        print(email, password)
    print("loop complete")
