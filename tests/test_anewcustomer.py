import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Homepage import HomePage
from PageObjects.newcuspage import NewCustomer
from TestData.Test_NewCustomerData import NewCustomerD
from utilities.BaseClass import BaseClass


class Testnew(BaseClass):

    def test_newcustomer(self, getData):
        logs = self.getLogger()
        homepage = HomePage(self.driver)
        logs.info("this is for checking text")
        check1 = homepage.homes().text
        check2 = homepage.mainheading().text
        print(check1)
        print(check2)
        assert "Home" in check1
        assert "XYZ Bank" in check2

        homepage.managerlogin().click()
        self.verifypresence("//*[contains(text(),'Add Customer')]")
        addcus = NewCustomer(self.driver)
        addcus.addcustomer().click()
        self.verifypresence("//*[contains(text(),'First Name :')]")


        addcus.firstname().send_keys(getData["firstname"])
        addcus.lastname().send_keys(getData["lastname"])
        addcus.pincode().send_keys(getData["pin"])
        addcus.finalbutton().click()

        alert = self.driver.switch_to.alert
        accountinfo = alert.text
        print(accountinfo)
        alert.accept()

        addcus.openaccount().click()
        self.verifypresence("//*[contains(text(),'Customer :')]")


        customer = Select(addcus.userselect())
        customer.select_by_visible_text(getData["fullname"])

        currency = Select(addcus.currency())
        currency.select_by_index(getData["index"])

        addcus.processbutton().click()
        alert1 = self.driver.switch_to.alert
        accountno = alert1.text
        print(accountno)
        alert1.accept()

        addcus.customerbutton().click()
        self.verifypresence("//*[@placeholder='Search Customer']")

        fn = addcus.retrivefirstname()
        for first in fn:
            if first.text == "saksh":
                fname = first.text
                print(fname)

        ln = addcus.retrivelastname()
        for last in ln:
            if last.text == "sinha":
                lname = last.text
                print(lname)

        an = addcus.retriveaccountnumber()
        for account in an:
            if account.text == "1016":
                acc = account.text
                print(acc)

        assert acc in accountno

        print("Hi " + fname + " " + lname + ",thanks for choosing this bank ,your account number is :" + str(acc))


    @pytest.fixture(params=NewCustomerD.test_Newcustomerdata)
    def getData(self, request):
        return request.param


