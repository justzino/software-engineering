from selenium import webdriver
import unittest
import time


class DemoUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('C:/programming/hongik-software-engineering/selenium/drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_GoogleSearch_Hongik(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Hongik University")
        self.driver.find_element_by_name("btnK").click()

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.close()
        cls.driver.quit()


print("Test Done Successfully!")
