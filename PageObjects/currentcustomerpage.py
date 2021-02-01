from selenium.webdriver.common.by import By


class CurrentCustomer:

    def __init__(self, driver):
        self.driver = driver

    Nselect = (By.XPATH, "//*[@name='userSelect']")
    login = (By.XPATH, "//*[@class='btn btn-default']")

    deposittab = (By.XPATH, "//*[@ng-class='btnClass2']")
    amountdeposit = (By.XPATH, "//*[@type='number']")
    depositbutton = (By.XPATH, "//*[@class='btn btn-default']")
    depositmessage= (By.XPATH, "//*[@ng-show='message']")

    withdrwaltab = (By.XPATH, "//*[@ng-class='btnClass3']")
    amountwithdraw = (By.XPATH, "//*[@type='number']")
    withdawbutton = (By.XPATH, "//*[@class='btn btn-default']")
    withdrawmessage = (By.XPATH, "//*[@ng-show='message']")

    transactiontab = (By.XPATH, "//*[@ng-class='btnClass1']")
    transactiondetails = (By.XPATH, "//*[@class='table table-bordered table-striped']")

    information = (By.XPATH, "(//*[@ng-hide='noAccount'])[2]")

    def nameselect(self):
        return self.driver.find_element(*CurrentCustomer.Nselect)
    def Login(self):
        return self.driver.find_element(*CurrentCustomer.login)
    def DepositTab(self):
        return self.driver.find_element(*CurrentCustomer.deposittab)
    def DepositAmount(self):
        return self.driver.find_element(*CurrentCustomer.amountdeposit)
    def DepositButton(self):
        return self.driver.find_element(*CurrentCustomer.depositbutton)
    def DepositMessage(self):
        return self.driver.find_element(*CurrentCustomer.depositmessage)
    def WithdrawTab(self):
        return self.driver.find_element(*CurrentCustomer.withdrwaltab)
    def AmountWithdraw(self):
        return self.driver.find_element(*CurrentCustomer.amountwithdraw)
    def WithdrawButton(self):
        return self.driver.find_element(*CurrentCustomer.withdawbutton)
    def WithdrawMessage(self):
        return self.driver.find_element(*CurrentCustomer.withdrawmessage)
    def TransactionTab(self):
        return self.driver.find_element(*CurrentCustomer.transactiontab)
    def TransactionDetails(self):
        return self.driver.find_element(*CurrentCustomer.transactiondetails)
    def Information(self):
        return self.driver.find_element(*CurrentCustomer.information)

