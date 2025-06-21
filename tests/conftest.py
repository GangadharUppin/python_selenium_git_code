import pytest
import logging
from selenium import webdriver
import tempfile
from selenium.webdriver.chrome.options import Options

# Create a session-level fixture to initialize the browser only once
@pytest.fixture(scope='session')
def session_driver():
    logging.info('[Session Setup] Launching browser...')
    # Create a temporary directory for user data
    user_data_dir = tempfile.mkdtemp()

    options = Options()
    options.add_argument(f'--user-data-dir={user_data_dir}')

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
