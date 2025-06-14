import pytest
import time
from pom.google_page import *
from utils import Utils



class TestGoogle:
    utils = Utils()


    def test_google(self):
        self.logging.info("Running test_google")
        self.driver.get("https://www.google.com")
        time.sleep(2)
        self.utils.is_ele_present(self.driver, google_icon)

    def test_flipkart_health_check(self, open_flipkart):
        self.logging.info("Flipkart health check test")
        time.sleep(6)
