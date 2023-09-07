---
title: "Deep Diff"
datePublished: Thu Sep 01 2022 23:05:00 GMT+0000 (Coordinated Universal Time)
cuid: cl7jnnd1b0d4g4xnv1om82lgw
slug: deep-diff
cover: https://cdn.hashnode.com/res/hashnode/image/unsplash/D9Zow2REm8U/upload/v1662071865209/BRyxFTS3k.jpeg
tags: python

---

**Installation:** pip install deepdiff

**Usage:** from deepdiff import DeepDiff

**Official Link:** [https://pypi.org/project/deepdiff/](Link)

**Docs:** [https://zepworks.com/deepdiff/5.8.1/](Link)

**DeepDiff** helps me a lot in **QA space**, especially in **API Testing**. In the below example, DeepDiff class takes in two arguments, i.e. two dictionaries, one with expected input and one with the actual output, And returns an DeepDiff object.

```python
expected = {1:1, 2:2, 3:3}
actual = {1:1, 2:3, 3:3}

def deepDiff():
    changes = DeepDiff(expected, actual)
    print('Type {}'.format(type(changes)))
    print('Changes {}'.format(changes))

deepDiff()
```

Output is shown in the below screenshot. We can print the changes and see the difference:

```python
Changes {'values_changed': {'root[2]': {'new_value': 3, 'old_value': 2}}}
```

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1662072663659/HXxLC7UOd.png align="left")