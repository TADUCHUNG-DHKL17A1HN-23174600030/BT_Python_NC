from xml.dom import minidom

# Tải file XML
doc = minidom.parse('sample.xml')

# in ra node name và node đầu tiên trong file
print(doc.nodeName)
print(doc.firstChild.tagName)


