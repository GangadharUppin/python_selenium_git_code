import pytest
import time
from pom.google_page import *
from utils import Utils



class TestGoogle:
    @pytest.mark.sanity
    def test_google(self):
        try:
            self.logging.info("Running test_google")
            self.driver.get("https://www.google.com")
            time.sleep(2)
            self.utils.is_ele_present(google_icon)
        except Exception as e:
            self.utils.fail_testcase("test_google", e)

    @pytest.mark.functional
    def test_flipkart_health_check(self, open_flipkart):
        try:
            self.logging.info("Flipkart health check test")
            time.sleep(6)
        except Exception as e:
            self.utils.fail_testcase("test_flipkart_health_check", e)
