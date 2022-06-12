from pages.home_page import Home
from pages.my_account_page import Account

class App():

    def __init__(self,driver):
        self.driver = driver

        self.home = Home(self.driver)
        self.account = Account(self.driver)