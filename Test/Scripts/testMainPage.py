import sys

sys.path.append(sys.path[0] + "/...")

from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.MainPage import MainPage
import unittest

class MainPage(WebDriverSetup):
    def testmainpage(self):
        driver = self.driver
        self.driver.get("https://www.dns-shop.ru/")
        self.driver.set_page_load_timeout(10)

        web_page_title = "DNS – интернет магазин цифровой и бытовой техники по доступным ценам."

        try:
            if driver.title == web_page_title:
                print("\nWebPage loaded succesfully")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            print(error + "WebPage failed to laod")
        mainpage = MainPage(driver)
if __name__ == '__main__':
    unittest.main()
