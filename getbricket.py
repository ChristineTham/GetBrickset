import SOAPpy
import xml.etree.ElementTree as ET

url = "http://brickset.com/api/v2.asmx?WSDL"
apikey = "LqqM-WlJg-Ik6b"
username = "ChristineTham"
password = "castle5052"

brickset = SOAPpy.WSDL.Proxy(url)
# brickset.show_methods()
args = brickset.methods['getThemes']
for p in args.inparams:
    print p.name, p.type
for p in args.outparams:
    print p.name, p.type
brickset.soapproxy.config.dumpSOAPOut = 1
brickset.soapproxy.config.dumpSOAPIn = 1
themes = brickset.getThemes(apiKey=apikey)
print len(themes), type(themes)
