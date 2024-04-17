import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from utilities.BaseClass import Baseclass


class TestHomePage(Baseclass):

    def test_formSubmission(self, getData):
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["Firstname"])
        homepage.getEmail().send_keys(getData["Email"])
        homepage.getPassword().send_keys(getData["Password"])
        homepage.getCheckBox().click()

        self.SelectOptionText(homepage.getGender(), getData["Gender"])

        homepage.getEmploymentStatus().click()
        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text
        print(alertText)
        assert "Success" in alertText
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
