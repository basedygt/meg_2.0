import sys
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options

class Meg:
    def __init__(self, wait=5, init_browser=True):
        self.wait = wait
        if init_browser:
            self.driver = self._initialize_browser()
        else:
            self.driver = input("\nPlease enter the driver object name: ")

    def _initialize_browser(self):
        options = Options()
        # options.headless = True  # Uncomment this line if you want to run in headless mode
        options.accept_insecure_certs = True
        return webdriver.Firefox(options=options)

    def fetch_source(self, url, output=None, imported=False):
        try:
            self.driver.get(url)
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
            if not imported:
                self.driver.quit()

    def fetch_sources(self, hosts_file, output=None):
        try:
            with open(hosts_file, "r") as f:
                host_lst = f.read().split("\n")
        except Exception as e:
            print(str(e))
            sys.exit(1)

        try:
            for host in host_lst:
                self.fetch_source(host, output, imported=True)

        except Exception as e:
            print(str(e))
            return None
        
        finally:
            self.driver.quit()
