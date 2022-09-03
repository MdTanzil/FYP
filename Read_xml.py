import xml.etree
import xml.etree.ElementTree as ET
import os


def extract_boxes(filename):
    tree = ET.parse(filename)

    root = tree.getroot()
    name = root.find('.//object/name').text
    return name

namelist = []
for count, f in enumerate(os.listdir()):
    if f == 'Read_xml.py.':
        continue
    
    name = extract_boxes(f)
    if name not in namelist: 
        namelist.append(name)    
        
print(namelist)


