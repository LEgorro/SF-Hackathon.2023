import pytest

from pages.labirint_page import LabirintPage
from pages.main_page import MainPage
from config.links import Links

class BaseTest:

    labirint_page: LabirintPage
    main_page: MainPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.main_page = MainPage(driver)