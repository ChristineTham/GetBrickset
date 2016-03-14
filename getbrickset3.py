import requests
import xml.etree.ElementTree as ET
import sys


url = "http://brickset.com/api/v2.asmx"
namespace = "http://brickset.com/api/"
apikey = "LqqM-WlJg-Ik6b"
username = "ChristineTham"
password = "castle5052"

getThemes = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <getThemes xmlns="http://brickset.com/api/">
      <apiKey>%s</apiKey>
    </getThemes>
  </soap:Body>
</soap:Envelope>
'''

session = requests.Session()

request = requests.Request("POST", url)
prepped = request.prepare()
prepped.body = getThemes % apikey
# print prepped.body
prepped.headers['Content-Type'] = "text/xml"
prepped.headers['Content-Length'] = len(prepped.body)
prepped.headers['SOAPAction'] = "http://brickset.com/api/getThemes"
# print prepped.headers

response = session.send(prepped)

if response.status_code != 200:
    print(response.text)
    sys.exit(1)
# print response.content
# Reads and parses the response
xml_response = ET.fromstring(response.content)

ns = {'ns0': "http://schemas.xmlsoap.org/soap/envelope/",
      'ns1': "http://brickset.com/api/"}

themes = xml_response.find('.//ns1:themes', ns)
ET.dump(themes)
