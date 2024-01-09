import allure
import pytest

from pages.main_page import MainPage
from pages.youtube_page import YoutubePage
from pages.telegram_bot_page import TelegramBotPage

class BaseTest:

    main_page: MainPage
    youtube_page: YoutubePage
    telegram_bot_page = TelegramBotPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.main_page = MainPage(driver)
        request.cls.youtube_page = YoutubePage(driver)
        request.cls.telegram_bot_page = TelegramBotPage(driver)