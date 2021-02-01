from selenium.webdriver.common.by import By


class NewCustomer:

    def __init__(self, driver):
        self.driver = driver

    addcus = (By.XPATH, "//*[contains(text(),'Add Customer')]")
    fname = (By.XPATH, "//*[@placeholder='First Name']")
    lname = (By.XPATH, "//*[@placeholder='Last Name']")
    pcode =(By.XPATH, "//*[@placeholder='Post Code']")
    fbutton = (By.XPATH, "(//*[contains(text(),'Add Customer')])[2]")
    oacc = (By.XPATH,"//*[contains(text(),'Open Account')]")
    uselect = (By.XPATH, "//*[@name='userSelect']")
    curr = (By.XPATH, "//*[@name='currency']")
    fbutton1 = (By.XPATH, "(//*[@type='submit'])[1]")
    cusbut = (By.XPATH, "//*[contains(text(),'Customers')]")
    cfname = (By.XPATH, "//*[@class='table table-bordered table-striped']/tbody/tr/td[1]")
    clname = (By.XPATH, "//*[@class='table table-bordered table-striped']/tbody/tr/td[2]")
    accno = (By.XPATH, "//*[@class='table table-bordered table-striped']/tbody/tr/td[4]")

    def addcustomer(self):
        return self.driver.find_element(*NewCustomer.addcus)
    def firstname(self):
        return self.driver.find_element(*NewCustomer.fname)
    def lastname(self):
        return self.driver.find_element(*NewCustomer.lname)
    def pincode(self):
        return self.driver.find_element(*NewCustomer.pcode)
    def finalbutton(self):
        return self.driver.find_element(*NewCustomer.fbutton)
    def openaccount(self):
        return self.driver.find_element(*NewCustomer.oacc)
    def userselect(self):
        return self.driver.find_element(*NewCustomer.uselect)
    def currency(self):
        return self.driver.find_element(*NewCustomer.curr)
    def processbutton(self):
        return self.driver.find_element(*NewCustomer.fbutton1)
    def customerbutton(self):
        return self.driver.find_element(*NewCustomer.cusbut)
    def retrivefirstname(self):
        return self.driver.find_elements(*NewCustomer.cfname)
    def retrivelastname(self):
        return self.driver.find_elements(*NewCustomer.clname)
    def retriveaccountnumber(self):
        return self.driver.find_elements(*NewCustomer.accno)