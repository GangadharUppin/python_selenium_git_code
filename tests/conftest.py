import os
import time

import pytest
import logging
from selenium import webdriver
import tempfile
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from pom.amazon_homepage import *
from utils import Utils

@pytest.fixture(scope='session')
def session_driver():
    logging.info('[Session Setup] Launching browser...')
    options = Options()

    temp_profile = tempfile.mkdtemp()
    options.add_argument(f'--user-data-dir={temp_profile}')

    # options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    logging.info('[Session Teardown] Closing browser...')
    driver.quit()


# Automatically applied to every class — inject driver/logging
@pytest.fixture(scope='class', autouse=True)
def auto_assign_driver(request, session_driver):
    request.cls.driver = session_driver
    request.cls.logging = logging
    utils = Utils(request.cls.logging, request.cls.driver)
    wait = WebDriverWait(request.cls.driver, 10)
    request.cls.wait = wait
    request.cls.utils = utils

@pytest.fixture(scope='class')
def open_flipkart(request, session_driver):
    logging.info(f'open flipkart setup')
    request.cls.driver.get("https://www.flipkart.com/")
    time.sleep(6)
    yield
    # request.cls.driver.close()
    logging.info(f'open flipkart teardown')

@pytest.fixture(scope='class')
def open_amazon(request, session_driver):
    logging.info(f'open amazon setup')
    request.cls.driver.get("https://www.amazon.com/")
    time.sleep(6)
    if request.cls.utils.is_ele_present(login):
        request.cls.utils.is_ele_present(login).click()
    yield
    # request.cls.driver.close()
    logging.info(f'open amazon teardown')

# conftest.py
def pytest_addoption(parser):
    parser.addoption("--item", action="store", default="iphone", help="Item to search on Amazon")
