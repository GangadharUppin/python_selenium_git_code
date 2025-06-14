from selenium import webdriver
import pytest
import time
import logging

@pytest.fixture(scope='class')
def session_driver(request):
    logging.info('setup of driver fixture.')
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    logging.info('teardown of driver fixture.')

