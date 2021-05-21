from selenium import webdriver
import unittest
import HtmlTestRunner
import time
import os


# chromedriver 경로 생성
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
chrome_path = r'\drivers\chromedriver.exe'
chrome_path = BASE_DIR + chrome_path
path_list = list(chrome_path.split('\\'))
chrome_path = "/".join(path_list)


class DemoUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(chrome_path)
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

if __name__ == '__main__':
    report_path = r'\reports'
    report_path = BASE_DIR + report_path
    tmp_list = list(report_path.split('\\'))
    report_path = "/".join(tmp_list)
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=report_path))
