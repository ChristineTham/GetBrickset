import SOAPpy
import xml.etree.ElementTree as ET

url = "http://www.webservicex.net/country.asmx?WSDL"
proxy = SOAPpy.WSDL.Proxy(url)
countries = ET.fromstring(proxy.GetCountries())
for country in countries.findall('./Table/Name'):
    print country.text

currencies = ET.fromstring(proxy.GetCurrencies())
ET.dump(currencies)
