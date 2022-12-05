import random
import time

from selenium.webdriver.common.by import By
import softest
from selenium.common import ElementNotSelectableException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import os

from datetime import datetime


class BaseDriver(softest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.action = ActionChains(driver)
        self.log = self.custom_logger()

    ######################### LOCATOR ACTIONS #####################

    def find_and_click(self, locator):
        self.wait_until_element_to_be_clickable(locator)
        element = self.driver.find_element(*locator)
        element.click()

    def find_and_mouseover(self, locator):
        self.wait_until_element_to_be_clickable(locator)
        element = self.driver.find_element(*locator)
        self.action.move_to_element(element).perform()

    def find_and_click_random_element(self, locator):
        self.wait_until_visibility_of_all_elements(locator)
        elements = self.driver.find_elements(*locator)
        random.choice(elements).click()

    def find_and_send(self, locator, value):
        self.wait_until_visibility_of_element(locator)
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def get_element_text(self, locator):
        self.wait_until_element_to_be_located(locator)
        element = self.driver.find_element(*locator)
        return element.text

    def create_an_element_by_link(self, link):
        return [By.XPATH, "//a[text()='" + link + "']"]

    ######################### ASSERTION ACTIONS #####################

    def assert_text_in_element(self, locator, text):
        element_text = self.get_element_text(locator)
        try:
            assert element_text.lower().__contains__(text.lower())
            self.log.info("Assertion accepted : " + element_text.lower() + " == " + text.lower())
        except Exception as e:
            self.log.error("Assertion declined : " + element_text.lower() + " != " + text.lower())
            raise e

    def assert_text_in_text(self, text1, text2):
        try:
            self.soft_assert(self.assertEqual, text1.lower(), text2.lower())
            self.log.info("Assertion accepted : " + text1.lower() + " == " + text2.lower())
        except Exception as e:
            self.log.error("Assertion declined : " + text1.lower() + " != " + text2.lower())
            raise e

    def assert_current_url(self, text):
        try:
            assert self.driver.current_url.lower().__contains__(text.lower())
            self.log.info("Assertion accepted : " + self.driver.current_url.lower() + " is contain " + text.lower())
        except Exception as e:
            self.log.error("Assertion declined : " + self.driver.current_url.lower() + " is not contain " + text.lower())
            raise e

    ################## WAITS #####################

    def wait_until_visibility_of_element(self, locator):
        self.wait.until(EC.visibility_of(self.driver.find_element(*locator)))

    def wait_until_visibility_of_all_elements(self, locator):
        self.wait.until(EC.visibility_of_all_elements_located(locator))

    def wait_until_element_to_be_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    def wait_until_element_attribute_text_to_be(self, locator, attribute, text):
        self.wait.until(EC.text_to_be_present_in_element_attribute(locator, attribute, text))

    def wait_until_element_to_be_located(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    ###################### LOGGER #####################

    def custom_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        # now = datetime.now()
        # dt_string = now.strftime("%d_%m_%Y")

        # test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        # filename_header = test_name[5:test_name.index('_', 5)]

        # filename = "../logs/CASE_" + filename_header + "_" + dt_string + ".log"

        # fh = logging.FileHandler(filename, mode='w')

        # formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(funcName)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S')

        # fh.setFormatter(formatter)
        # logger.addHandler(fh)
        return logger
