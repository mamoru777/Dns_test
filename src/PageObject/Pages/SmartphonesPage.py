import sys
sys.path.append(sys.path[0] + "/....")

from selenium.webdriver.common.by import By
from src.PageObject.Locators import Locator


class Smartphones(object):
    def __init__(self, driver):
        self.driver = driver
        self.Izbran = driver.find_element(By.CLASS_NAME, Locator.Izbran)

    def getPrices(self, id):
        return self.driver.find_element(By.XPATH, Locator.getPrices(self, id))

    def getLike(self, id):
        return self.driver.find_element(By.XPATH, Locator.Like(self, id))
