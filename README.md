# meg_2.0
Fetch the HTML sources loaded in the DOM using a live browser

### Description

Because Tomnom's Meg can't presently collect sources with any JavaScript updates, it may miss a lot of crucial information. To fix that, I built a little script [meg_2.0](https://github.com/basedygt/meg_2.0).

### Usage

```python
from meg import Meg

browser = Meg("https://example.com/")
dom_source = browser.load_source(output="source.html", wait=5)
print(dom_source)
```
