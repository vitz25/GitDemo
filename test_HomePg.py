from PageObjects.HomePage import HomePage
from utilities.BaseClass import Baseclass


class TestHomePage(Baseclass):

    def test_formSubmission(self):
        homepage = HomePage(self.driver)
        homepage.getName().send_keys("Vitesh Gadewar")
        homepage.getEmail().send_keys("viteshgadewar@gmail.com")
        homepage.getPassword().send_keys("V!tesh25797")
        homepage.getCheckBox().click()

        self.SelectOptionText(homepage.getGender(), "Male")

        homepage.getEmploymentStatus().click()
        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text
        print(alertText)
        assert "Success" in alertText
