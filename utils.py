import os

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import subprocess
import os


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
            base_dir = os.path.join(os.getcwd(), "screenshots")
            # Create folder if not exists
            os.makedirs(base_dir, exist_ok=True)
            # Save screenshot using OS-independent path
            screenshot_path = os.path.join(base_dir, "is_ele_present.png")
            self.driver.save_screenshot(screenshot_path)
            return None

    def fail_testcase(self, name_of_image, exception_is):
        base_dir = os.path.join(os.getcwd(), "screenshots")
        # Create folder if not exists
        os.makedirs(base_dir, exist_ok=True)
        # Save screenshot using OS-independent path
        screenshot_path = os.path.join(base_dir, f"{name_of_image}.png")
        self.driver.save_screenshot(screenshot_path)
        raise Exception(f'Failed with exception: {exception_is}')


    # def generate_allure_report(self, results_dir="allure-results", report_dir="allure-report"):
    #     # Make sure the results directory exists
    #     if not os.path.exists(results_dir):
    #         os.makedirs(results_dir, exist_ok=True)
    #
    #     # Call the allure CLI from Python
    #     try:
    #         subprocess.run(["allure", "generate", results_dir, "-o", report_dir, "--clean"], check=True)
    #         self.logging.info(f"Allure report successfully generated at: {report_dir}")
    #     except subprocess.CalledProcessError as e:
    #         self.logging.info(f"Failed to generate Allure report: {e}")

