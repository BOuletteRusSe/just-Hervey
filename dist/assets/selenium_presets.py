
from selenium import webdriver

class Driver:
    
    def __init__(self, headless: bool=False):
        
        self.executable_path = r'assets\chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-software-rasterizer")
        if headless:
            self.options.add_argument("--headless")
            self.options.add_argument("--disable-gpu")
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
