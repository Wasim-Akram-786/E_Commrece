
from POM.LoginPage import LoginPage
from selenium import webdriver


class test_001:
    email="admin@yourstore.com"
    password="admin"



    def test_login(self,setup):
        self.driver=setup