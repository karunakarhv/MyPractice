---
title: "Python Tips and Tricks"
datePublished: Sat Sep 05 2020 15:41:26 GMT+0000 (Coordinated Universal Time)
cuid: ckepu4hlm02p6kps19cuw2idg
slug: python-tips-and-tricks
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1600647137743/2MgKuTxgk.jpeg

---

## Traceback - Print or retrieve a stack traceback

```python
import traceback
traceback.print_stack()
```

#### Reference:

Traceback \[ https://docs.python.org/2/library/traceback.html \]

## Timestamp in milliseconds

```python
from datetime import datetime
def timestampMillisec():
    now = datetime.now()
    return int((now - now.replace(hour=0, 
                                  minute=0, 
                                  second=0, 
                                  microsecond=0))
               .total_seconds()*1000)
```