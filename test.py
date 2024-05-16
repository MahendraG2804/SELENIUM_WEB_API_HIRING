from library.basic_selenium_actions import *
from library.comparison_actions import *
from Constants.xpath.topgrephire import *
from Constants.xpath.art_of_testing import *
from library.exeception_handlers import *
from Constants.xpath.saucedemo import *
from library.data_helper import *
from library.vedio_recorder import recording
import multiprocessing
# from basic_functions import *
import time 


def main():
        #Start the rcording in the seperate processers
        recording_process = multiprocessing.Process(target=recording)
        recording_process.start()
        
        
        # import csv
        # data =[]
        # with open("C:/Users/User/OneDrive/Desktop/Selenium_LMS/Constants/data/saucedemo_login.csv") as csvfile:
        #     reader = csv.DictReader(csvfile)
        #     for row in reader:
        #         data.append(row)
                # print(row)
        
        
        # data = read_csv_data("C:/Users/User/OneDrive/Desktop/Selenium_LMS/Constants/data/saucedemo_login.csv")
        data = read_mysql_data("select user_name, password from cust where user_name ='standard_user'")
        # driver = open_browser( "https://artoftesting.com/samplesiteforselenium", headless=True)
        driver = open_browser( "https://www.saucedemo.com/")
        time.sleep(5)
        # wait_until_element_is_visible(driver, lnk_link_text)
        # take_screenshot(driver)
        # time.sleep(5)
        # take_screenshot(driver, "first_screenshot.png")
        # expect_error(driver, wait_until_element_is_visible, "sdfgbgfr")


        # click_element(driver, "//button[@type='button']")
        # time.sleep(5)
        # enter_text_in_element(driver, "//input[@name='firstName']", "Automation")
        # time.sleep(5)
        # scroll_element_into_view(driver,"//select[contains(@id, 'testingDropdown')]")
        # time.sleep(5)
        # select_value_in_dropdown(driver,
        #                          "//select[contains(@id, 'testingDropdown')]",
        #                          "Manual")
        # time.sleep(5)
        # click_element(driver,"//button[contains(text(), 'Alert Box')]" )
        # time.sleep(5)
        # alert_text = handle_alert(driver)
        # time.sleep(5)
        # print(f" The alert text was {alert_text}.")

        # wait_until_element_is_visible(driver, btn_gen_alert_box)
        # click_element(driver, btn_gen_alert_box)
        # time.sleep(5)
        # alert_text = handle_alert(driver)
        # time.sleep(5)
        # print(f'the alert text is {alert_text}')
        # time.sleep(5)
        # alert_text = handle_alert(driver)
        # print(f"the alert text was {alert_text}.")

        # wait_until_element_is_visible(driver, lnk_link_text)
        # should_contain(driver, lnk_link_text, "link")
        # should_be_equal(driver, lnk_link_text, "This is a link")
        # should_contain(driver, lnk_link_text, "topgrep")
        # continue_on_failure(driver, should_contain, lnk_link_text, "link")
        # continue_on_failure(driver, should_contain, lnk_link_text, "topgrep")


        wait_until_element_is_visible(driver, txt_box_username)
        print('jiiuh',data)
        # if data is not None:
        #     # Access elements of data
        #     enter_text_in_element(driver, txt_box_username, data[0]['txt_box_username'])
        # else:
        #     print("Data is None. Make sure it is properly initialized.")

        # if data is not None:
        #     # Access elements of data
        #     enter_text_in_element(driver, txt_box_password, data[0]['txt_box_password'])
        # else:
        #     print("Data is None. Make sure it is properly initialized.")

        # enter_text_in_element(driver, txt_box_username, data[0]['txt_box_username'])
        # enter_text_in_element(driver, txt_box_password, data[0]['txt_box_password'])

        enter_text_in_element(driver, txt_box_username, data[0])
        enter_text_in_element(driver, txt_box_password, data[1])


        click_element(driver, btn_login)
        time.sleep(2)
        wait_until_element_is_visible(driver, lnk_backpack)
        click_element(driver, lnk_backpack )
        wait_until_element_is_clickable(driver, btn_add_to_cart)
        time.sleep(2)
        # for _ in range (int(data[0]['number_of_items'])):
        #     print(3)
        #     # click_element(driver, btn_add_to_cart)
        click_element(driver, btn_add_to_cart)  
        wait_until_element_is_visible(driver, btn_remove)
        time.sleep(10)



        recording_process.terminate()
        #Quit the WebDriver
        driver.quit()

# main method
if __name__ == "__main__":
        main()