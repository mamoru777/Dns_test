import sys
sys.path.append(sys.path[0] + "/...")
import unittest
import time
from src.TestBase.WebDriverSetup import WebDriverSetup
from selenium.webdriver.common.keys import Keys
from src.PageObject.Pages.MainPage import MainPage
from src.PageObject.Pages.SmartphonesPage import Smartphones
from src.PageObject.Pages.Smartphones_and_photo import Smartphones_and_photo


class testPrices(WebDriverSetup):
    def testPrices(self):
        driver = self.driver
        self.driver.get('https://www.dns-shop.ru/')
        #self.driver.set_page_load_timeout(10)

        main = MainPage(driver)
        #home.Smartphones_and_photo.hover()
        #time.sleep(2)
        main.Smartphones_and_photo.click()
        #time.sleep()
        driver = self.driver
        smap = Smartphones_and_photo(driver)
        smap.Smartphones.click()
        driver = self.driver
        sm = Smartphones(driver)
        driver.execute_script("window.scrollTo(0, window.scrollY + 300)")
        time.sleep(2)
        sm.getPrices(1).click()
        sm.getPrices(2).click()
        sm.getPrices(3).click()
        sm.getPrices(4).click()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()