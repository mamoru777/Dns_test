import sys

sys.path.append(sys.path[0] + "/...")

import unittest
import time
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.SmartphonePage import Smartphone
from src.PageObject.Pages.SmartphoneWithCommentPage import SmartphoneWithCommentPage
from src.PageObject.Pages.CommentPage import CommentPage

class testComment(WebDriverSetup):
    def testComment(self):
        driver = self.driver
        self.driver.get('https://www.dns-shop.ru/product/5429da9af387ed20/61-smartfon-apple-iphone-13-128-gb-cernyj/')
        sm = Smartphone(driver)
        driver.execute_script("window.scrollTo(0, window.scrollY + 700)")
        time.sleep(2)
        sm.Comments.click()
        time.sleep(3)
        self.driver.get('https://www.dns-shop.ru/opinion-page/add/?objectId=5429da9a-f387-11ec-8fdc-00155d8ed20c&objectType=610d4c8e-37fc-416c-a603-bce518d57c15')
        driver = self.driver
        cm = CommentPage(driver)
        cm.Stars.click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        time.sleep(2)
        cm.Input_button.click()
        time.sleep(10)
