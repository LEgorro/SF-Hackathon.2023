from selenium.webdriver.support import expected_conditions as EC

from base.base_page import BasePage

class TelegramBotPage(BasePage):
    PAGE_URL = "https://t.me/PriyatniyIldar_bot"

    channel = ("xpath", "(//div/a[@class='tgme_action_button_new shine'])")

    def channel_is_clickable(self):
        self.wait.until(EC.element_to_be_clickable(self.channel))
