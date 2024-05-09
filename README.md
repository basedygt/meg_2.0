# meg_2.0
Fetch the HTML sources loaded in the DOM using a live browser

### Description

Because Tomnom's Meg can't presently collect sources with any JavaScript updates, it may miss a lot of crucial information. To fix that, I built a little script [meg_2.0](https://github.com/basedygt/meg_2.0).

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

authenticate before fetching

```python
from meg import Meg

"""
Your code to authenticate here
"""

browser = Meg(wait=5, init_browser=False)
browser.fetch_sources("urls.txt", output_dir="output")
