import time

import pytest
import logging
from selenium import webdriver
import tempfile
from selenium.webdriver.chrome.options import Options

from pom.amazon_homepage import *
from utils import Utils


# Create a session-level fixture to initialize the browser only once
@pytest.fixture(scope='session')
def session_driver():
    logging.info('[Session Setup] Launching browser...')
    temp_profile = tempfile.mkdtemp()
    options = Options()

    # Ensuring a unique user-data-dir
    options.add_argument(f"--user-data-dir={temp_profile}")
    # it is required when running from docker
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")

    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--window-size=1920,1080")  # Important for rendering
    
    driver = webdriver.Chrome(options=options)
    yield driver
    logging.info('[Session Teardown] Closing browser...')
    driver.quit()


# Automatically applied to every class — inject driver/logging
@pytest.fixture(scope='class', autouse=True)
def auto_assign_driver(request, session_driver):
    request.cls.driver = session_driver
    request.cls.logging = logging
    utils = Utils(request.cls.logging, request.cls.driver)
    request.cls.utils = utils

@pytest.fixture(scope='class')
def open_flipkart(request, session_driver):
    logging.info(f'open flipkart setup')
    request.cls.driver.get("https://www.flipkart.com/")
    yield
    # request.cls.driver.close()
    logging.info(f'open flipkart teardown')

@pytest.fixture(scope='class')
def open_amazon(request, session_driver):
    logging.info(f'open amazon setup')
    request.cls.driver.get("https://www.amazon.com/")
    if request.cls.utils.is_ele_present(login):
        request.cls.utils.is_ele_present(login).click()

    yield
    # request.cls.driver.close()
    logging.info(f'open amazon teardown')
