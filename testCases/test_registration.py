import time

import allure
import pytest
from pageObjects.registrationPageObjects import RegistrationPage
from utilities.excel_reader import get_excel_test_data
from utilities.logger import get_logger
from utilities.data_generator import generate_random_gmail


@allure.severity(allure.severity_level.NORMAL)
class TestRegistration():
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_registration_form_with_existing_emailid(self,setup):
        self.driver=setup
        rp=RegistrationPage(self.driver)
        req_message=(rp.enterFirstName("Dileep")
         .enterLastName("Kumar")
         .enterEmail("abc@abc.com")
         .enterPhoneNumber("1234567891")
         .enterPassword("root@123")
         .enterConfirmPassword("root@123")
         .clickSubscribeRadioCheckBox()
         .clickPolicyCheckBox()
         .clickContinueButtonForErrorMessage())
        assert "Warning: E-Mail Address is already registered!"!=req_message

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_wanted_fail_scenario(self,setup):
        self.driver=setup
        rp=RegistrationPage(self.driver)
        req_message=(rp.enterFirstName("Dileep")
         .enterLastName("Kumar")
         .enterEmail("abc@abc.com")
         .enterPhoneNumber("1234567891")
         .enterPassword("root@123")
         .enterConfirmPassword("root@123")
         .clickSubscribeRadioCheckBox()
         .clickPolicyCheckBox()
         .clickContinueButton().getSuccessMessage())
        assert "I am testcase 2"==req_message

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    @pytest.mark.parametrize("test_data", get_excel_test_data("register"))
    def test_registration_form(self,setup,test_data):
        email = generate_random_gmail()
        self.driver=setup
        rp=RegistrationPage(self.driver)
        req_success_message=(rp.enterFirstName(test_data["firstname"])
         .enterLastName(test_data["lastname"])
         .enterEmail(email)
         .enterPhoneNumber(test_data["phone"])
         .enterPassword(test_data["password"])
         .enterConfirmPassword(test_data["confirmpassword"])
         .clickSubscribeRadioCheckBox()
         .clickPolicyCheckBox()
         .clickContinueButton().getSuccessMessage())
        assert "Your Account Has Been Created!"==req_success_message

