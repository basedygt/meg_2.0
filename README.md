# meg_2.0
Fetch the HTML sources loaded in the DOM using a live browser

### Description

Because Tomnom's Meg can't presently collect sources with any JavaScript updates, it may miss a lot of crucial information. To fix that, I built a little script [meg_2.0](https://github.com/basedygt/meg_2.0/blob/main/meg.py).

### Usage

Fetch single url

```python
from meg import Meg

url = "http://example.org"
browser = Meg(wait=5)
dom_source = browser.fetch_source(url, output="source.html")
print(dom_source)
```

Fetch multiple urls

```python
from meg import Meg

browser = Meg(wait=5)
browser.fetch_sources("urls.txt", output_dir="output")
```

Authenticate before fetching

```python
from meg import Meg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Your code to authenticate here, example:
ff = webdriver.Firefox()
ff.find_element_by_id('username').send_keys('your_username')
ff.find_element_by_id('password').send_keys('your_password')
ff.find_element_by_id('remember_me').click()
ff.find_element_by_id('login_button').click()
ff.implicitly_wait(5)

# run the instance with custom browser
browser = Meg(wait=5, init_browser=False, custom_driver="ff")
browser.fetch_sources("urls.txt", output_dir="output")
```
