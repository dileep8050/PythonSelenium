from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from utilities.logger import get_logger

logger = get_logger()

class LoggedActions:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def send_keys(self, by, value, input_text):
        logger.info(f"Typing into element ({by}, {value}): {input_text}")
        element = self.wait.until(EC.visibility_of_element_located((by, value)))
        element.clear()
        element.send_keys(input_text)

    def click(self, by, value):
        logger.info(f"Clicking on element ({by}, {value})")
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    def clear(self, by, value):
        logger.info(f"Clearing input field ({by}, {value})")
        element = self.wait.until(EC.visibility_of_element_located((by, value)))
        element.clear()

    def get_text(self, by, value):
        logger.info(f"Getting text from element ({by}, {value})")
        text = self.wait.until(EC.visibility_of_element_located((by, value))).text
        logger.info(f"Text retrieved: {text}")
        return text

    def get_attribute(self, by, value, attribute_name):
        logger.info(f"Getting attribute '{attribute_name}' from element ({by}, {value})")
        element = self.wait.until(EC.presence_of_element_located((by, value)))
        attr = element.get_attribute(attribute_name)
        logger.info(f"Attribute value: {attr}")
        return attr

    def is_displayed(self, by, value):
        element = self.wait.until(EC.presence_of_element_located((by, value)))
        result = element.is_displayed()
        logger.info(f"Element ({by}, {value}) is displayed: {result}")
        return result

    def is_enabled(self, by, value):
        element = self.wait.until(EC.presence_of_element_located((by, value)))
        result = element.is_enabled()
        logger.info(f"Element ({by}, {value}) is enabled: {result}")
        return result

    def is_selected(self, by, value):
        element = self.wait.until(EC.presence_of_element_located((by, value)))
        result = element.is_selected()
        logger.info(f"Element ({by}, {value}) is selected: {result}")
        return result

    def wait_until_visible(self, by, value):
        logger.info(f"Waiting until element ({by}, {value}) is visible")
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def wait_until_clickable(self, by, value):
        logger.info(f"Waiting until element ({by}, {value}) is clickable")
        return self.wait.until(EC.element_to_be_clickable((by, value)))

    def hover_over(self, by, value):
        logger.info(f"Hovering over element ({by}, {value})")
        element = self.wait.until(EC.visibility_of_element_located((by, value)))
        ActionChains(self.driver).move_to_element(element).perform()

    def scroll_into_view(self, by, value):
        logger.info(f"Scrolling to element ({by}, {value})")
        element = self.wait.until(EC.presence_of_element_located((by, value)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def double_click(self, by, value):
        logger.info(f"Double clicking on element ({by}, {value})")
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        ActionChains(self.driver).double_click(element).perform()

    def right_click(self, by, value):
        logger.info(f"Right clicking on element ({by}, {value})")
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        ActionChains(self.driver).context_click(element).perform()

    def execute_script(self, script, *args):
        logger.info(f"Executing JavaScript: {script}")
        return self.driver.execute_script(script, *args)

    def take_screenshot(self, file_path):
        logger.info(f"Taking screenshot and saving to: {file_path}")
        self.driver.save_screenshot(file_path)
