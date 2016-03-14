from suds.client import Client
import csv


url = "http://brickset.com/api/v2.asmx?WSDL"
namespace = "http://brickset.com/api/"
apikey = "LqqM-WlJg-Ik6b"
username = "ChristineTham"
password = "castle5052"

brickset = Client(url)
# print brickset
themes = brickset.service.getThemes(apikey)
theme = themes['themes'][0]
with open("themes.csv", 'wb') as csvfile:
    csvwriter = csv.DictWriter(csvfile, brickset.dict(theme).keys().sort(), dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(["theme", "setCount", "subthemeCount", "yearFrom", "yearTo"])
    for theme in themes['themes']:
        csvwriter.writerow([theme.theme, theme.setCount, theme.subthemeCount, theme.yearFrom, theme.yearTo])
