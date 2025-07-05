import pytest
import time

from selenium.webdriver.common.by import By

from pom.amazon_homepage import *
from pom.google_page import *
from utils import Utils

class Test_Amazon:
    @pytest.mark.sanity
    def test_open_amazon(self):
        self.logging.info("Amazon health check test")
        self.driver.get("https://www.amazon.com")
        time.sleep(1)

    @pytest.mark.functional
    def test_amazon_title(self, open_amazon):
        self.logging.info("amazon health check test")
        time.sleep(6)
        # self.logging.info(f"Title of amazon page is{self.driver.title}")
        # self.driver.find_element(By.XPATH, search_bar).send_keys("iphone")
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, search_icon).click()
        # time.sleep(2)
