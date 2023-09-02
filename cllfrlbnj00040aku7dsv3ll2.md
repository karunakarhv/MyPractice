---
title: "Crack the Code: Reading XML Files the Python Way"
datePublished: Thu Aug 17 2023 23:00:12 GMT+0000 (Coordinated Universal Time)
cuid: cllfrlbnj00040aku7dsv3ll2
slug: crack-the-code-reading-xml-files-the-python-way
cover: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/ZIPFteu-R8k/upload/20894a23d4fb78d2ba4dc1da49f60a52.jpeg
tags: xml, python, python-beginner

---

To read an XML file in Python, you can use the `ElementTree` module, which is part of the standard library. The `ElementTree` module allows you to parse XML data easily and navigate through its elements. Here's a step-by-step guide on how to read an XML file in Python:

1. Import the required modules:
    

```python
import xml.etree.ElementTree as ET
```

1. Load the XML file:
    

```python
tree = ET.parse('path/to/your/file.xml')
```

1. Get the root element of the XML tree:
    

```python
root = tree.getroot()
```

1. Access XML data and perform operations as needed. You can traverse the XML tree using methods like `find`, `findall`, and `iter` to extract specific elements and attributes.
    

Example XML file (data.xml):

```python
<fruits>
    <fruit name="Apple">
        <color>Red</color>
        <taste>Sweet</taste>
    </fruit>
    <fruit name="Banana">
        <color>Yellow</color>
        <taste>Sweet</taste>
    </fruit>
    <fruit name="Orange">
        <color>Orange</color>
        <taste>Citrus</taste>
    </fruit>
</fruits>
```

Example Python code to read the XML file:

```python
import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('data.xml')

# Get the root element
root = tree.getroot()

# Access and print data
for fruit in root.findall('fruit'):
    name = fruit.get('name')
    color = fruit.find('color').text
    taste = fruit.find('taste').text
    print(f"{name}: color={color}, taste={taste}")
```

Output:

```python
Apple: color=Red, taste=Sweet
Banana: color=Yellow, taste=Sweet
Orange: color=Orange, taste=Citrus
```

That's it! You can now read and extract data from the XML file using Python. Make sure to adjust the file path to your specific XML file when using the `ET.parse()` function.