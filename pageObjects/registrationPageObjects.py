# from selenium.webdriver.common.by import By
# from pageObjects.loginPageObjects import LoginPage
#
#
# class RegistrationPage:
#     txt_firstName_id="input-firstname"
#     txt_lastName_id="input-lastname"
#     txt_email_id="input-email"
#     txt_phone_id="input-telephone"
#     txt_password_id="input-password"
#     txt_confirmPassword_id="input-confirm"
#     radiobtn_subscribe_xpath="//label[normalize-space()='Yes']"
#     checkbox_policy_xpath="//input[@name='agree']"
#     btn_continue_css=".btn.btn-primary"
#     lbl_ErrorText_css=".alert.alert-danger.alert-dismissible"
#     link_myaccount_xpath="//span[text()='My Account']"
#     link_login_xpath="//li/a[text()='Login']"
#
#     def __init__(self,driver):
#         self.driver=driver
#
#     def enterFirstName(self,firstName):
#         self.driver.find_element(By.ID,self.txt_firstName_id).send_keys(firstName)
#         return self
#
#     def enterLastName(self,lastName):
#         self.driver.find_element(By.ID,self.txt_lastName_id).send_keys(lastName)
#         return self
#     def enterEmail(self,email):
#         self.driver.find_element(By.ID,self.txt_email_id).send_keys(email)
#         return self
#     def enterPhoneNumber(self,phoneNumber):
#         self.driver.find_element(By.ID,self.txt_phone_id).send_keys(phoneNumber)
#         return self
#     def enterPassword(self,password):
#         self.driver.find_element(By.ID,self.txt_password_id).send_keys(password)
#         return self
#     def enterConfirmPassword(self,confirmPassword):
#         self.driver.find_element(By.ID,self.txt_confirmPassword_id).send_keys(confirmPassword)
#         return self
#     def clickSubscribeRadioCheckBox(self):
#         self.driver.find_element(By.XPATH,self.radiobtn_subscribe_xpath).click()
#         return self
#     def clickPolicyCheckBox(self):
#         self.driver.find_element(By.XPATH,self.checkbox_policy_xpath).click()
#         return self
#     def clickContinueButton(self):
#         self.driver.find_element(By.CSS_SELECTOR,self.btn_continue_css).click()
#         return self
#     def getErrorMessage(self):
#         return self.driver.find_element(By.CSS_SELECTOR,self.lbl_ErrorText_css)
#     def clickMyAccountLink(self):
#         self.driver.find_element(By.XPATH,self.link_myaccount_xpath).click()
#         return self
#     def clickLoginLink(self):
#         self.driver.find_element(By.XPATH,self.link_login_xpath).click()
#         return LoginPage(self.driver)



from selenium.webdriver.common.by import By

from pageObjects.registerSuccessPage import RegisterSuccessPage
from utilities.wrapped_actions import LoggedActions
from pageObjects.loginPageObjects import LoginPage

class RegistrationPage:
    txt_firstName_id = "input-firstname"
    txt_lastName_id = "input-lastname"
    txt_email_id = "input-email"
    txt_phone_id = "input-telephone"
    txt_password_id = "input-password"
    txt_confirmPassword_id = "input-confirm"
    radiobtn_subscribe_xpath = "//label[normalize-space()='Yes']"
    checkbox_policy_xpath = "//input[@name='agree']"
    btn_continue_css = ".btn.btn-primary"
    lbl_ErrorText_css = ".alert.alert-danger.alert-dismissible"
    link_myaccount_xpath = "//span[text()='My Account']"
    link_login_xpath = "//li/a[text()='Login']"

    def __init__(self, driver):
        self.driver = driver
        self.actions = LoggedActions(driver)

    def enterFirstName(self, firstName):
        self.actions.send_keys(By.ID, self.txt_firstName_id, firstName)
        return self

    def enterLastName(self, lastName):
        self.actions.send_keys(By.ID, self.txt_lastName_id, lastName)
        return self

    def enterEmail(self, email):
        self.actions.send_keys(By.ID, self.txt_email_id, email)
        return self

    def enterPhoneNumber(self, phoneNumber):
        self.actions.send_keys(By.ID, self.txt_phone_id, phoneNumber)
        return self

    def enterPassword(self, password):
        self.actions.send_keys(By.ID, self.txt_password_id, password)
        return self

    def enterConfirmPassword(self, confirmPassword):
        self.actions.send_keys(By.ID, self.txt_confirmPassword_id, confirmPassword)
        return self

    def clickSubscribeRadioCheckBox(self):
        self.actions.click(By.XPATH, self.radiobtn_subscribe_xpath)
        return self

    def clickPolicyCheckBox(self):
        self.actions.click(By.XPATH, self.checkbox_policy_xpath)
        return self

    def clickContinueButtonForErrorMessage(self):
        return self.actions.click(By.CSS_SELECTOR,self.btn_continue_css)

    def clickContinueButton(self):
        self.actions.click(By.CSS_SELECTOR, self.btn_continue_css)
        return RegisterSuccessPage(self.driver)

    # def getRegistrationErrorMessage(self):
    #     return self.actions.get_text(By.CSS_SELECTOR, self.lbl_ErrorText_css)

    def clickMyAccountLink(self):
        self.actions.click(By.XPATH, self.link_myaccount_xpath)
        return self

    def clickLoginLink(self):
        self.actions.click(By.XPATH, self.link_login_xpath)
        return LoginPage(self.driver)
