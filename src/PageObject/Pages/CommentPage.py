import sys
sys.path.append(sys.path[0] + "/....")

from selenium.webdriver.common.by import By
from src.PageObject.Locators import Locator

class CommentPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.Stars = driver.find_element(By.XPATH, Locator.Stars)
        #self.Dost = driver.find_element(By.CLASS_NAME, Locator.Dost)
        self.Input_button = driver.find_element(By.XPATH, Locator.Input_button)