import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CheckoutPage import CheckOutPage
from PageObjects.HomePage import HomePage
from utilities.BaseClass import Baseclass

class Test():
    pass

class Testone(Baseclass):

    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkOutPage = homepage.shopItems()
        log.info("Getting all the card titles")
        cards = checkOutPage.getCardTitles()

        i = -1

        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()
                break

        checkOutPage.precheckout().click()
        confirmPage = checkOutPage.checkOutItems()

        log.info("Entering Country Name")

        confirmPage.Insertkey().send_keys("ind")
        self.verifyLinkPresence("India")
        confirmPage.Country().click()
        confirmPage.Checkbox().click()
        confirmPage.Purchase().click()
        SuccessText = confirmPage.SuccessText().text
        log.info("text received from the application is" + SuccessText)

        assert "Success! Thank you!" in SuccessText
