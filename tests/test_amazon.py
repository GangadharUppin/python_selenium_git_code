import pytest
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pom.amazon_homepage import *
from pom.google_page import *
from utils import Utils
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def item_to_search(request):
    return request.config.getoption("--item")

@pytest.mark.usefixtures("open_amazon")
class Test_Amazon:
    @pytest.mark.sanity
    def test_open_amazon(self):
        try:
            self.logging.info("Amazon health check test")
            self.driver.get("https://www.amazon.com")
            time.sleep(1)
        except Exception as e:
            self.logging.info(f'TC failed with exception: {e}')
            self.utils.fail_testcase("test_search_item", e)

    @pytest.mark.sanity
    def test_amazon_title(self):
        try:
            self.logging.info(f"Title of amazon page is = {self.driver.title}")
            self.driver.find_element(By.XPATH, search_bar).send_keys("iphone")
            time.sleep(2)
            self.driver.find_element(By.XPATH, search_icon).click()
            time.sleep(2)
        except Exception as e:
            self.logging.info(f'TC failed with exception: {e}')
            self.utils.fail_testcase("test_search_item", e)

    @pytest.mark.functional
    def test_number_of_cart_items(self):
        """
        It is using ID
        :return:
        """
        try:
            text = self.driver.find_element(By.ID, amazon_cart_items).text
            self.logging.info(f'number of items in cart is: {text}')
        except Exception as e:
            self.logging.info(f'TC failed with exception: {e}')
            self.utils.fail_testcase("test_search_item", e)


    @pytest.mark.functional
    @pytest.mark.xfail
    def test_search_item(self, item_to_search):
        """
        It is using explicit  wait
        :return:
        """
        first_laptop = "//img[contains(@src, 'https://m.media-amazon.com/images/I/815uX7wkOZS._AC_UY218_.jpg')]"
        try:
            self.logging.info("Start of Test case.")
            self.driver.find_element(By.XPATH, search_bar).send_keys(item_to_search)
            self.driver.find_element(By.XPATH, search_icon).click()
            self.wait.until(EC.element_to_be_clickable(self.utils.is_ele_present(first_laptop)))
        except Exception as e:
            self.logging.info(f"Testcase failed with exception: {e}")
            self.utils.fail_testcase("test_search_item", e)


    @pytest.mark.xsanity
    def test_implicit_wait(self):
        try:
            self.driver.implicitly_wait(10)
            self.driver.find_element(By.XPATH, "//a[@aria-label='Amazon']")
        except Exception as e:
            self.utils.fail_testcase("test_implicit_wait", e)


    @pytest.mark.functional
    def test_web_element_methods(self):
        """
        for example suppose if we use get_attribute() it will fetch always from html DOM page
        Suppose druning run time any value changed , if we use get_property() it will fetch
        changed value. not from HTML
        it uses updated value .
        """
        try:
            self.driver.implicitly_wait(10)
            ele = self.driver.find_element(By.XPATH, "//a[@aria-label='Amazon']")
            self.logging.info(f'ele attribute is as : {ele.get_attribute("aria-label")}')
            self.logging.info(f'ele pro is as 1: {ele.get_property("href")}')
        except Exception as e:
            self.utils.fail_testcase("test_implicit_wait", e)

    @pytest.mark.functional
    def test_action_chains(self):
        try:
            # for workarond
            self.driver.refresh()
            ele = self.wait.until(EC.visibility_of_element_located((By.XPATH, amazon_signin)))
            action_chain = ActionChains(self.driver)
            action_chain.move_to_element(ele).perform()
            time.sleep(5)
            elements = self.driver.find_elements(By.XPATH, elements_amazon_sign_in)
            for ele_text in elements:
                self.logging.info(f'text on element is: {ele_text.text}')
        except Exception as e:
            self.logging.info(f"Testcase failed with exception: {e}")
            self.utils.fail_testcase("test_action_chains", e)
