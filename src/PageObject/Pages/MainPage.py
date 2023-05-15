import sys
sys.path.append(sys.path[0] + "/....")

from selenium.webdriver.common.by import By
from src.PageObject.Locators import Locator


class MainPage(object):
    def __init__(self, driver):
        self.driver = driver
        # self.logo = driver.find_element(By.CLASS_NAME, Locator.logo)
        self.search_input = driver.find_element(By.CLASS_NAME, Locator.search_input)
        self.search_button = driver.find_element(By.CLASS_NAME, Locator.search_button)
        self.Smartphones_and_photo = driver.find_element(By.XPATH, Locator.Smarphones_and_photo)

    def getResult(self, word):
        results = self.driver.find_elements(By.XPATH, Locator.Titles)
        for result in results:
            if word.lower() in result.text.lower():
                return True
        return False

    def getSearch(self):
        return self.driver.find_element(By.CLASS_NAME, Locator.Error).text
        #self.Login = driver.find_element(By.CLASS_NAME, Locator.Button_enter)
        #self.smartphones = driver.find_element(By.XPATH, Locator.Smartphones)
