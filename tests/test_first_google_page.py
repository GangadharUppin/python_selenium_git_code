import pytest
import time
from pom.google_page import *
from utils import Utils


@pytest.mark.usefixtures("session_driver")
class TestGoogle:
    utils = Utils()

    def test_googl(self):
        self.driver.get("https://www.google.com")
        time.sleep(2)
        self.utils.is_ele_present(self.driver, google_icon)

