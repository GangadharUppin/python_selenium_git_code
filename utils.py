from selenium import webdriver
from selenium.webdriver.common.by import By


class Utils:

    def is_ele_present(self, driver ,element):
        # //*[local-name()='svg' and @class='lnXdpd']
        status = driver.find_element(By.XPATH, element)
        if status:
            return status
        else:
            return None
