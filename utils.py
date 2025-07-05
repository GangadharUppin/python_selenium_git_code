from selenium import webdriver
from selenium.webdriver.common.by import By


class Utils:
    def __init__(self, logging, driver):
        self.logging = logging
        self.driver = driver

    def is_ele_present(self,element):
        # //*[local-name()='svg' and @class='lnXdpd']
        status = self.driver.find_element(By.XPATH, element)
        self.logging.info(f'status is : {status}')
        if status:
            return status
        else:
            self.logging.info(f'ele not found')
            self.driver.save_screenshot("page.png")
            return None
