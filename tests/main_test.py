import pytest
import allure

from config.links import Links
from base.base_test import BaseTest
from pages.main_page import MainPage

@allure.feature("Links to social networks")
class TestMainPage(BaseTest):

    @allure.title("Header YouTube link work")
    @allure.severity("Medium")
    @pytest.mark.smoke
    def test_header_youtube_link_work(self):
        self.main_page.open()
        self.main_page.header_youtube_link_work()

    def test_header_twitch_link_work(self):
        self.main_page.open()
        self.main_page.header_twitch_link_work()

    def test_meet_TG_bot_btn_work(self):
        self.main_page.open()
        self.main_page.meet_TG_bot_button_work()

