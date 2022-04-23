import selenium

# Create class for storing POM based  attributes and action method

class LoginPage:
    email_xpath="// input[ @ id = 'Email']"
    password_xpath="//input[@id='Password']"
    login_xpath="//button[contains(text(),'Log in')]"

    def __init__(self,driver):
        self.driver=driver

    def setemail(self,email):
        self.driver.find_element_by_xpath(self.email_xpath).clear()
        self.driver.find_element_by_xpath(self.email_xpath).send_keys(email)

    def set_password(self,password):
        self.driver.find_element_by_xpath(self.password_xpath).clear()
        self.driver.find_element_by_xpath(self.password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_xpath).click


