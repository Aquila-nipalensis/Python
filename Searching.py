import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Searching(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://google.com/ncr')

    def test_searching(self):
        field = self.driver.find_element_by_name('q')
        field.send_keys('selenide')
        field.send_keys(Keys.RETURN)
        result = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/div/div[1]/a/div/cite')
        assert 'selenide.org' in result.get_attribute('innerHTML')
        image = self.driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[2]/a')
        image.click()
        imageresult = self.driver.find_element_by_xpath('//*[@id="rg_s"]/div[1]/a[2]/div[2]')
        assert 'selenide.org' in imageresult.get_attribute('innerHTML')
        all_search = self.driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[1]/a')
        all_search.click()
        result = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/div/div[1]/a/div/cite')
        assert 'selenide.org' in result.get_attribute('innerHTML')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
