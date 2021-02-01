from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    home = (By.XPATH, "//*[@class='btn home']")
    heading = (By.XPATH, "//*[@class='mainHeading']")
    login1 = (By.XPATH, "//*[contains(text(),'Bank Manager Login')]")
    login2 = (By.XPATH, "//*[contains(text(),'Customer Login')]")

    def homes(self):
        return self.driver.find_element(*HomePage.home)
    def mainheading(self):
        return  self.driver.find_element(*HomePage.heading)
    def managerlogin(self):
        return self.driver.find_element(*HomePage.login1)
    def customerlogin(self):
        return self.driver.find_element(*HomePage.login2)