from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Utils:
    def __init__(self, logging, driver):
        self.logging = logging
        self.driver = driver

    def is_ele_present(self,element):
        # //*[local-name()='svg' and @class='lnXdpd']
        status = None
        try:
            status = self.driver.find_element(By.XPATH, element)
            self.logging.info(f'status is : {status}')
            if status:
                return status
        except NoSuchElementException:
            self.logging.info(f'element is not found : {status}')
            self.driver.save_screenshot("page.png")
            return None
