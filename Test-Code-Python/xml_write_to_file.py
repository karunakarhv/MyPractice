from lxml import etree as ET

cbrsParams = ET.Element("cbrsParams")
registrationParams = ET.SubElement(cbrsParams, "registrationParams")
cbsdSerialNo = ET.SubElement(registrationParams, "cbsdSerialNumber")
cbsdSerialNo.text='12345'

tree = ET.ElementTree(cbrsParams)
tree.write('cbsdc1.xml', pretty_print=True, xml_declaration=True, encoding="utf-8")