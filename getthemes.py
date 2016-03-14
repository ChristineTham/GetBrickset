from suds.client import Client
import csv


url = "http://brickset.com/api/v2.asmx?WSDL"
namespace = "http://brickset.com/api/"
apikey = "LqqM-WlJg-Ik6b"
username = "ChristineTham"
password = "castle5052"

brickset = Client(url)


def write_csv(filename, objects):
    global brickset
    fieldnames = sorted(brickset.dict(objects[0]).keys())
    with open(filename, 'wb') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames,
                                   dialect='excel',
                                   quoting=csv.QUOTE_NONNUMERIC)
        csvwriter.writeheader()
        for object in objects:
            csvwriter.writerow(brickset.dict(object))

def open_csv(filename, object):
    global brickset
    fieldnames = sorted(brickset.dict(object).keys())
    csvfile = open(filename, 'wb')
    csvwriter = csv.DictWriter(csvfile, fieldnames,
                               dialect='excel',
                               quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writeheader()
    return csvfile, csvwriter

def append_csv(csvwriter, objects):
    for object in objects:
        csvwriter.writerow(brickset.dict(object))

# print brickset
themes = brickset.service.getThemes(apikey)['themes']
write_csv("themes.csv", themes)

csvfile, csvwriter = open_csv("subthemes.csv", brickset.factory.create('subthemes'))

for theme in themes:
     subthemes = brickset.service.getSubthemes(apikey, theme.theme)[0]
     append_csv(csvwriter, subthemes)

csvfile.close()
