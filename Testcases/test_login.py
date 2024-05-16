import pytest
from Testcases.configtest import setup
from selenium import webdriver
from scripts.LoginPage import Login

class Test_001_Login:
    baseURL ="https://qa-hiring.topgrep.com/"
    email="hiring_robot_auto_test@getnada.com"
    password="hiring_robot_auto_test@getnada.coM"
    
    def test_homePageTitle(self, setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        actual_title=self.driver.title
        self.driver.close()
        # if actual_title=="Welcome to AIVAGAM":
        if actual_title=="AIVAGAM - Platform for QA":
            assert True
        else:
            assert False
            
    def test_login(self, setup):
        self.driver= setup
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)
        self.lp.clickSignin()
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        self.driver.close()
        # if act_title=="Job Board":
        #     assert True
        # else:
        #     assert False 
    
