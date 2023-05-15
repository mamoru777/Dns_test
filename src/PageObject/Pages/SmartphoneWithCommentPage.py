import sys
sys.path.append(sys.path[0] + "/....")

from selenium.webdriver.common.by import By
from src.PageObject.Locators import Locator

class SmartphoneWithCommentPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.AddComment = driver.find_element(By.XPATH, Locator.AddComment)