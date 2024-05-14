import sys
import time
import os
import re

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options

class Meg:
    def __init__(self, wait=5, init_browser=True, custom_driver=None):
        self.wait = wait
        if init_browser:
            self.driver = self._initialize_browser()
        else:
            self.driver = custom_driver

    def _initialize_browser(self):
        options = Options()
        # options.headless = True  # Uncomment this line if you want to run in headless mode
        options.accept_insecure_certs = True
        return webdriver.Firefox(options=options)

    def fetch_source(self, url, output=False, imported=False):
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

    def fetch_sources(self, hosts_file, output_dir):
        try:
            with open(hosts_file, "r") as f:
                host_lst = f.read().split("\n")
        except Exception as e:
            print(str(e))
            sys.exit(1)

        try:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            for host in host_lst:
                pretty_html = self.fetch_source(host, imported=True)
                if pretty_html:
                    filename = self._url_to_filename(host)
                    output_path = os.path.join(output_dir, filename)
                    with open(output_path, "w") as f:
                        f.write(pretty_html)

        except Exception as e:
            print(str(e))
            return None
        
        finally:
            self.driver.quit()

    def _url_to_filename(self, url):
        # Remove illegal characters from the URL and replace them with underscores
        filename = re.sub(r'[<>:"/\\|?*]', '_', url)
        return filename
