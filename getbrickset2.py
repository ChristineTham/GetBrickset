import SOAPpy
import xml.etree.ElementTree as ET


url = "http://brickset.com/api/v2.asmx"
namespace = "http://brickset.com/api/"
apikey = "LqqM-WlJg-Ik6b"
username = "ChristineTham"
password = "castle5052"

brickset = SOAPpy.SOAPProxy(url, namespace)
brickset.config.dumpSOAPOut = 1
brickset.config.dumpSOAPIn = 1
themes = brickset.getThemes(apiKey=apikey)
print themes
