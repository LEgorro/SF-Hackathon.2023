import pytest
import allure

from config.links import Links
from base.base_test import BaseTest
from pages.main_page import MainPage

@allure.feature("Links to social networks")
class TestMainPage(BaseTest):

    @allure.title("Header YouTube link work")
    @allure.severity("Normal")
    @allure.link(name = "Testing page", url = "https://dima731515.github.io/hakaton/html/")
    @pytest.mark.smoke
    def test_header_youtube_link_work(self):
        self.main_page.open()
        self.main_page.header_youtube_link_work()

    @allure.title("Header Twitch link work")
    @allure.severity("Normal")
    @allure.link(name = "Testing page", url = "https://dima731515.github.io/hakaton/html/")
    @pytest.mark.smoke
    def test_header_twitch_link_work(self):
        self.main_page.open()
        self.main_page.header_twitch_link_work()

    @allure.title('"Meet Telegram bot" button work')
    @allure.severity("Critical")
    @allure.link(name = "Testing page", url = "https://dima731515.github.io/hakaton/html/")
    @pytest.mark.smoke
    def test_meet_TG_bot_btn_work(self):
        self.main_page.open()
        self.main_page.meet_TG_bot_button_work()

