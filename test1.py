
from library.basic_selenium_actions import *
from library.comparison_actions import *
from Constants.xpath.topgrephire import *
from library.exeception_handlers import *
from library.data_helper import *

from selenium.webdriver.common.keys import Keys
from library.vedio_recorder import recording
import multiprocessing
# from basic_functions import *
import time 

def main():

#*********************************Login Flow**************************************#

    driver=open_browser("https://qa-hiring.topgrep.com/")
    time.sleep(1)
    click_element(driver, btn_singin)
    enter_text_in_element(driver, txt_box_email, "hiring_robot_auto_test@getnada.com")
    time.sleep(1)
    # driver.implicitly_wait(20)
    enter_text_in_element(driver, txt_box_password, "hiring_robot_auto_test@getnada.coM")
    time.sleep(1)
    click_element(driver, btn_login)
    time.sleep(1)

#********************************** Post A Job ***************************************#
    
    click_element(driver, btn_add_jobs)
    time.sleep(1)
    enter_text_in_element(driver, txt_box_job_title, "Multi Tasker Admin Role")
    time.sleep(1)
    enter_text_in_element(driver, txt_box_job_loc, "PUNE")
    time.sleep(1)
    enter_text_in_element(driver, txt_box_job_qualify, "ANY DEGREE With Age below 50")
    time.sleep(1)
    enter_text_in_element(driver, txt_box_job_responsble, "We seek to employ a young highly dynamic and self-motivated multi tasker person who can bring the following to the business")
    time.sleep(1)
    enter_text_in_element(driver, txt_box_job_desc, "We are an Australian Group dealing in manufacturing/Importing of Sporting Goods, Customised Sublimation Sports/Fashion Wear & Fabrics , Selling Van Car Accessories & Installations at our factory in Moorabbin 3189 Our partner is also a psychic medium.")
    time.sleep(1)
    click_element(driver, drop_down_clk_emp_type)
    time.sleep(1)
    click_element(driver, drop_down_emp_type_contract)
    time.sleep(1)
    enter_text_in_element(driver, select_skills, "selenium")
    time.sleep(1)
    driver.find_element(By.XPATH, select_skills).send_keys(Keys.PAGE_DOWN)
    # driver.find_element_by_name("Value").send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, select_skills).send_keys(Keys.ENTER)
    time.sleep(1)
    click_element(driver, btn_create_posting)
    time.sleep(5)





# main method
if __name__ == "__main__":
        main()