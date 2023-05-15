import sys
sys.path.append(sys.path[0] + "/....")

from selenium.webdriver.common.by import By
from src.PageObject.Locators import Locator

class Smartphone(object):
    def __init__(self, driver):
        self.driver = driver
        self.Comments = driver.find_element(By.XPATH, Locator.Commenets)

