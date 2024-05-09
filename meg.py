import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Meg:

    def __init__(self, url, wait=5):
        self.driver = self._initialize_browser()
        self.url = url
        self.wait = wait

    def _initialize_browser(self):
        options = Options()
#       options.headless = True
        options.accept_insecure_certs = True
        return webdriver.Firefox(options=options)

    def load_source(self, output=None):
        try:
            self.driver.get(self.url)
            time.sleep(self.wait)
            dom_html = self.driver.execute_script("return document.documentElement.outerHTML;")
            soup = BeautifulSoup(dom_html, 'html.parser')
            pretty_html = soup.prettify()

            if output:
                with open(output, "w") as f:
                    f.write(pretty_html)

            return pretty_html
        except TimeoutException:
            print("Timeout occurred while loading the page.")
            return None
        finally:
            self.driver.quit()
