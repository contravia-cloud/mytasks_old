import xml.etree.ElementTree as ET

tree = ET.parse('dataOpen.xml')
root = tree.getroot()
print(root)
for child in root:
    print(child.tag, child.attrib)

