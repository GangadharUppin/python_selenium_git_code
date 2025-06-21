import pytest
import logging
from selenium import webdriver
import tempfile
from selenium.webdriver.chrome.options import Options

# Create a session-level fixture to initialize the browser only once
@pytest.fixture(scope='session')
def session_driver():
    logging.info('[Session Setup] Launching browser...')
    options = Options()

    # Headless mode (optional, can be disabled)
    options.add_argument("--headless=new")

    # Recommended for Docker/CI/Linux environments
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Use a clean user-data-dir
    temp_profile = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={temp_profile}")
    driver = webdriver.Chrome(options=options)
    yield driver
    logging.info('[Session Teardown] Closing browser...')
    driver.quit()


# Automatically applied to every class — inject driver/logging
@pytest.fixture(scope='class', autouse=True)
def auto_assign_driver(request, session_driver):
    request.cls.driver = session_driver
    request.cls.logging = logging

@pytest.fixture(scope='class')
def open_flipkart(request, session_driver):
    logging.info(f'open flipkart setup')
    request.cls.driver.get("https://www.flipkart.com/")
    yield
    request.cls.driver.close()
    logging.info(f'open flipkart teardown')



#
