import sys
sys.path.append(sys.path[0] + "/....")

from selenium.webdriver.common.by import By
from src.PageObject.Locators import Locator

class Smartphones_and_photo(object):
    def __init__(self, driver):
        self.driver = driver
        self.Smartphones = driver.find_element(By.XPATH, Locator.Smartphones)
        #self.Smartphones_and_Gadzhet = driver.find_element(By.XPATH, Locator.Smartphones_and_Gadzhet)