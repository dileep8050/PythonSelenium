import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
import os
import threading
import base64
import pytest_html
import re
from utilities.config_reader import ConfigReader
from utilities.logger import get_logger

# Thread-local storage for WebDriver
_driver = threading.local()
config = ConfigReader()




def strip_ansi_codes(text):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

@pytest.fixture(scope="function")
def setup(browser_platform):
    """Create a new WebDriver instance per test function (thread-safe)."""
    browser = config.get("browser")
    base_url = config.get("base_url")
    baseenv = config.get("execution_env")
    wait_time = int(config.get("implicit_wait"))
    browser, platform = browser_platform

    if baseenv == "remote":
        options = {
            "chrome": webdriver.ChromeOptions,
            "edge": webdriver.EdgeOptions,
            "firefox": webdriver.FirefoxOptions
        }
        platform_mapping = {"windows": "WIN10", "mac": "MAC", "linux": "LINUX"}
        platform_name = platform_mapping.get(platform)
        opt = options[browser]()
        opt.add_experimental_option("detach", True) if browser in ["chrome", "edge"] else None
        opt.platform_name = platform_name
        _driver.instance = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", options=opt)
    elif baseenv == "local":
        if browser == "chrome":
            opt = webdriver.ChromeOptions()
            opt.add_experimental_option("detach", True)
            _driver.instance = webdriver.Chrome(options=opt)
        elif browser == 'firefox':
           options = webdriver.FirefoxOptions()
           _driver.instance = webdriver.Firefox(options=options)
           print("Launching Firefox browser.........")
        elif browser == 'edge':
           options = webdriver.EdgeOptions()
           options.add_experimental_option("detach", True)
           _driver.instance = webdriver.Edge(options=options)
           print("Launching Edge browser.........")
        else:
            raise ValueError(f"Unsupported browser: {browser}")
    _driver.instance.implicitly_wait(wait_time)
    _driver.instance.get(base_url)
    _driver.instance.maximize_window()
    yield _driver.instance
    _driver.instance.quit()


# CLI argument hook
def pytest_addoption(parser):
   parser.addoption("--browser",default="firefox")
   parser.addoption("--os",default="linux")

# Fixture to fetch browser option
@pytest.fixture()
def browser_platform(request):
   browser =  request.config.getoption("--browser")
   os =  request.config.getoption("--os")
   return browser, os

def get_driver():
    """Get WebDriver instance for current thread."""
    return getattr(_driver, 'instance', None)

def _capture_screenshot_base64():
    """Capture screenshot as Base64 string."""
    driver = get_driver()
    if driver:
        return driver.get_screenshot_as_base64()
    return None

@pytest.hookimpl(hookwrapper=True)  # No tryfirst here
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    logger = get_logger()
    extra = getattr(report, "extra", [])

    if report.when == "call":
        if report.passed:
            logger.info(f"✅ Test PASSED: {item.nodeid}")
        elif report.failed:
            if call.excinfo:
                exception_type = call.excinfo.type.__name__
                exception_message = str(call.excinfo.value)
                exception_message_clean = strip_ansi_codes(exception_message)
                logger.error(f"Exception Type: {exception_type}")
                logger.error(f"Exception Message: {exception_message_clean}")

            logger.error(f"❌ Test FAILED: {item.nodeid}")
            # ✅ Allure Screenshot attachment (only this line added)
            driver = get_driver()
            if driver:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"{item.name}",
                    attachment_type=AttachmentType.PNG
                )
            screenshot_base64 = _capture_screenshot_base64()

            if screenshot_base64:
                html = (
                    f'<div><img src="data:image/png;base64,{screenshot_base64}" '
                    f'alt="screenshot" style="width:304px;height:228px;cursor:pointer;" '
                    f'onclick="var win=window.open();'
                    f'var img=win.document.createElement(\'img\');'
                    f'img.src=this.src;'
                    f'img.style.width=\'100vw\';'
                    f'img.style.height=\'100vh\';'
                    f'img.style.objectFit=\'contain\';'
                    f'img.style.margin=\'0\';'
                    f'img.style.padding=\'0\';'
                    f'img.style.display=\'block\';'
                    f'win.document.body.style.margin=\'0\';'
                    f'win.document.body.style.overflow=\'hidden\';'
                    f'win.document.body.appendChild(img);" align="right"/></div>'
                )
                extra.append(pytest_html.extras.html(html))
        elif report.skipped:
            logger.warning(f"⚠️ Test SKIPPED: {item.nodeid}")

    report.extra = extra


def pytest_html_report_title(report):
    """Custom HTML report title."""
    report.title = "Automation Test Report"

@pytest.fixture(scope="function", autouse=True)
def log_test_case_start_end(request):
    logger = get_logger()
    test_name = request.node.nodeid
    logger.info(f"🔷 START: {test_name}")
    yield
    logger.info(f"🔶 END: {test_name}")