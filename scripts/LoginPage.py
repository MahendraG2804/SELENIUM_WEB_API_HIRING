from selenium import webdriver
from Constants.xpath.topgrephire import *
from selenium.webdriver.common.by import By
import time 

class Login:
    btn_signin_xpath = btn_singin
    txtbox_email_xpath = txt_box_email
    txtbox_pwd_xpath = txt_box_password
    btn_login_xpath = btn_login
    btn_logout_xpath = "eeer"

    def __init__(self, driver):
        self.driver = driver

    def clickSignin(self):
        self.driver.find_element(By.XPATH, self.btn_signin_xpath).click()

        # self.driver.find_element_by_xpath(self.btn_signin_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtbox_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtbox_email_xpath).send_keys(email)

        # self.driver.find_element_by_xpath(self.txtbox_email_xpath).clear()
        # self.driver.find_element_by_xpath(self.txtbox_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtbox_pwd_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtbox_pwd_xpath).send_keys(password)

        # self.driver.find_element_by_xpath(self.txtbox_pwd_xpath).clear()
        # self.driver.find_element_by_xpath(self.txtbox_pwd_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

        # self.driver.find_element_by_xpath(self.btn_login_xpath).click()