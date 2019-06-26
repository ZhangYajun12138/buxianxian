from time import sleep
import unittest
from selenium import webdriver

class BaiduSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.driver.get('https://www.baidu.com')

    def tearDown(self) -> None:
        self.driver.close()

    def test_baidu_search(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        sleep(1)
        self.driver.find_element_by_id('su').click()
        sleep(1)
        try:
            assert "selenium1" in self.driver.title
            print("Test Pass.")
        except Exception as e:
            print("Test Failed.",format(e))

if __name__ == '__main__':
    unittest.main()