import pytest
import time
from pom.google_page import *
from utils import Utils

class Test_Amazon:
    def test_open_amazon(self, open_amazon):
        self.logging.info("Amazon health check test")
        time.sleep(1)
