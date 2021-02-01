import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Homepage import HomePage
from PageObjects.currentcustomerpage import CurrentCustomer
from TestData.TestData_Existingcustomer import Existing
from utilities.BaseClass import BaseClass


class Testexisting(BaseClass):

    def test_existingcus(self, getData):
        logs = self.getLogger()
        homepage = HomePage(self.driver)
        logs.info("This is the log")
        check1 = homepage.homes().text
        check2 = homepage.mainheading().text

        print(check1)
        print(check2)

        assert "Home" in check1
        assert "XYZ Bank" in check2

        homepage.customerlogin().click()

        self.verifypresence("//*[contains(text(),'Your Name :')]")
        currentcus= CurrentCustomer(self.driver)
        cus_name = Select(currentcus.nameselect())
        ld = cus_name.select_by_index(getData["index"])
        self.verifypresence("//*[@class='btn btn-default']")

        currentcus.Login().click()

        self.verifypresence("//*[contains(text(),' Welcome ')]")

        info = currentcus.Information().text
        print(info)

        currentcus.DepositTab().click()

        self.verifypresence("//*[contains(text(),'Amount to be Deposited :')]")

        currentcus.DepositAmount().send_keys(getData["Amountdeposit"])
        currentcus.DepositButton().click()
        mess = currentcus.DepositMessage().text
        print(mess)
        info1 = currentcus.Information().text
        print(info1)

        assert "Deposit Successful" in mess

        currentcus.WithdrawTab().click()

        self.verifypresence("//*[contains(text(),'Amount to be Withdrawn :')]")

        currentcus.AmountWithdraw().send_keys(getData["Amountwithdraw"])
        currentcus.WithdrawButton().click()
        mess1 = currentcus.WithdrawMessage().text
        print(mess1)
        assert "Transaction successful" in mess1

        info2 = currentcus.Information().text
        print(info2)

        currentcus.TransactionTab().click()

        self.verifypresence("//*[contains(text(),'Reset')]")

        transaction = currentcus.TransactionDetails().text
        print(transaction)


    @pytest.fixture(params=Existing.test_existingdata)
    def getData(self,request):
        return request.param