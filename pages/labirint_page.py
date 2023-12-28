import time

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class LabirintPage(BasePage):

    PAGE_URL = "https://www.labirint.ru"

    search_field = ("xpath", "//form[@id='searchform']")
    btn_find = ("xpath", "//button[@form='searchform']")
    search_text = ("xpath", "//h1[@class = 'index-top-title']")
    def enter_search_form(self):
        search_field1 = self.wait.until(EC.visibility_of_element_located(self.search_field))
        time.sleep(3)
        search_field1.send_keys('race')
        time.sleep(3)

    def click_find_button(self):
        self.wait.until(EC.element_to_be_clickable(self.btn_find)).click()

    def is_search_work(self, query):
        self.wait.until(EC.visibility_of_element_located(self.search_text))