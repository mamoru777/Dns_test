import sys

sys.path.append(sys.path[0] + "/...")
import unittest
import time
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.SmartphonesPage import Smartphones

class testLike(WebDriverSetup):
    def testLike(self):
        driver = self.driver
        self.driver.get('https://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/')
        sm = Smartphones(driver)
        driver.execute_script("window.scrollTo(0, window.scrollY + 300)")
        time.sleep(3)
        sm.getLike(1).click()
        sm.getLike(2).click()
        sm.getLike(3).click()
        time.sleep(3)
        sm.Izbran.click()
        time.sleep(5)
