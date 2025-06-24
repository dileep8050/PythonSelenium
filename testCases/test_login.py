import pytest
import allure

from pageObjects.registrationPageObjects import RegistrationPage

@allure.severity(allure.severity_level.CRITICAL)
class TestLogin:
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_loginPage(self,setup):
        self.driver=setup
        rp = RegistrationPage(self.driver)
        error_msg_invalid=(rp.clickMyAccountLink()
         .clickLoginLink()
         .enterUsername('aaaaaa@bbb.com')
         .enterPwd('dummy')
         .clickLogin()
         .getErrorMessage())
        assert "Warning: No match for E-Mail Address and/or Password."==error_msg_invalid