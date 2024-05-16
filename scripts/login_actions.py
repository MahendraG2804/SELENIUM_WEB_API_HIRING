from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from library.basic_selenium_actions import *
from Constants.xpath.topgrephire import *
from Constants.xpath.aivagam import *
import time

def login(driver, email, password):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "hero_signInButton__usnj3")]')))
    click_element(driver, btn_singin)
    enter_text_in_element(driver, txt_box_email, email)
    time.sleep(1)
    enter_text_in_element(driver, txt_box_password, password)
    time.sleep(1)
    click_element(driver, btn_login)
    time.sleep(1)

def scholar_login(driver, email, password):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[normalize-space()='AIVAGAM']")))
    click_element(driver, A_btn_signin)
    enter_text_in_element(driver, A_txtbox_email, "mahendraqa@getnada.com")
    time.sleep(1)
    enter_text_in_element(driver, A_txtbox_password, "mahendraqa@getnada.coM")
    time.sleep(1)
    click_element(driver, A_btn_login)
    time.sleep(1)
