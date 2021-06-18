from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class WebDriver :

    def __init__(self , page_url):
        self.page_url= page_url

    def driver (self):
        option = Options()
        option.add_argument("start-maximized")
        #changer votre path de chromedriver dans "executable_path"
        browser = webdriver.Chrome(executable_path=r"C:\chromedriver.exe", options=option)
        browser.get(self.page_url)
        return browser