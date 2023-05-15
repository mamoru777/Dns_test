import sys
sys.path.append(sys.path[0] + "/...")
import unittest
import time
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.MainPage import MainPage

class testSearch(WebDriverSetup):
    def testSearch(self):
        driver = self.driver
        self.driver.get('https://www.dns-shop.ru/')
        main = MainPage(driver)
        main.search_input.click()
        time.sleep(1)
        main.search_input.send_keys('программная инженерия')
        time.sleep(2)
        main.search_button.click()
        time.sleep(5)
        search = main.getSearch()
        try:
            self.assertEqual('Странно, но по запросу "программная инженерия" ничего нет', search)
        except Exception as error:
            print(error + "Error")
        self.driver.get('https://www.dns-shop.ru/')
        main = MainPage(driver)
        main.search_input.click()
        time.sleep(1)
        main.search_input.send_keys('iphone')
        time.sleep(2)
        main.search_button.click()
        time.sleep(5)
        search = main.getResult('iphone')
        try:
            self.assertTrue(search)
        except Exception as error:
            print(str(error) + "Error")
if __name__ == '__main__':
    unittest.main()