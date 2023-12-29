import allure

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):

    PAGE_URL = "https://dima731515.github.io/hakaton/html/"

    header_youtube_link = ("xpath", f"//a[@href = '{Links.YOUTUBE}']")
    youtube_logo = ("xpath", "(//yt-icon[@id='logo-icon'])[1]")
    header_twitch_link = ("xpath", f"//a[@href = '{Links.TWITCH}']")
    btn_meet_TG_bot = ("xpath", "//section/a[@class='call-to-action__button button']")
    btn_get_prophecy = ("xpath", "(//a[@href = 'https://t.me/PriyatniyIldar_bot'])[1]")

    @allure.step("Click on YouTube logo in header")
    def header_youtube_link_work(self):
        self.wait.until(EC.element_to_be_clickable(self.header_youtube_link)).click()

    @allure.step("Click on Twitch logo in header")
    def header_twitch_link_work(self):
        self.wait.until(EC.element_to_be_clickable(self.header_twitch_link)).click()

    @allure.step('Click on "Get Prophecy" button')
    def prophecy_button_work(self):
        button = self.wait.until(EC.element_to_be_clickable(self.btn_get_prophecy)).click()
        self.driver.execute_script("arguments[0].click();", button)

    @allure.step('Click on "Meet Telegram bot" button')
    def meet_TG_bot_button_work(self):
        button = self.wait.until(EC.element_to_be_clickable(self.btn_meet_TG_bot))
        self.driver.execute_script("arguments[0].click();", button)