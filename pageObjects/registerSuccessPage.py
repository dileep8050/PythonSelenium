from utilities.wrapped_actions import LoggedActions
from selenium.webdriver.common.by import By

class RegisterSuccessPage:

    lbl_success_msg_css = "#content h1"

    def __init__(self, driver):
        self.actions = LoggedActions(driver)

    def getSuccessMessage(self):
        return self.actions.get_text(By.CSS_SELECTOR,self.lbl_success_msg_css)


