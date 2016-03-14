from BricksetAPIv2_services import *
import sys

loc = BricksetAPIv2Locator()

# prints messages sent and received if tracefile is set
kw = { 'tracefile' : sys.stdout }
portType = loc.getBricksetAPIv2Soap(**kw)

request = getSetsSoapIn()
request._apiKey = 'LqqM-WlJg-Ik6b'

response = portType.getSets(request)
