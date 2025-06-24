# from selenium.webdriver.common.by import By
#
# class LoginPage():
#     txt_username_id="input-email"
#     txt_password_id="input-password"
#     btn_login_css="form .btn.btn-primary"
#     lbl_errormsg_css=".alert-danger.alert-dismissible"
#
#     def __init__(self,driver):
#         self.driver=driver
#     def enterUsername(self,username):
#         self.driver.find_element(By.ID,self.txt_username_id).send_keys(username)
#         return self
#     def enterPwd(self,password):
#         self.driver.find_element(By.ID,self.txt_password_id).send_keys(password)
#         return self
#     def clickLogin(self):
#         self.driver.find_element(By.CSS_SELECTOR, self.btn_login_css).click()
#         return self
#     def getErrorMessage(self):
#         return self.driver.find_element(By.CSS_SELECTOR, self.lbl_errormsg_css).text
#


from selenium.webdriver.common.by import By
from utilities.wrapped_actions import LoggedActions

class LoginPage:
    txt_username_id = "input-email"
    txt_password_id = "input-password"
    btn_login_css = "form .btn.btn-primary"
    lbl_errormsg_css = ".alert-danger.alert-dismissible"

    def __init__(self, driver):
        self.driver = driver
        self.actions = LoggedActions(driver)

    def enterUsername(self, username):
        self.actions.send_keys(By.ID, self.txt_username_id, username)
        return self

    def enterPwd(self, password):
        self.actions.send_keys(By.ID, self.txt_password_id, password)
        return self

    def clickLogin(self):
        self.actions.click(By.CSS_SELECTOR, self.btn_login_css)
        return self

    def getErrorMessage(self):
        return self.actions.get_text(By.CSS_SELECTOR, self.lbl_errormsg_css)
