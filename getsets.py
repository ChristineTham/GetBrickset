from suds.client import Client
import unicodecsv


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
        csvwriter = unicodecsv.DictWriter(csvfile, fieldnames,
                                   dialect='excel',
                                   quoting=unicodecsv.QUOTE_NONNUMERIC)
        csvwriter.writeheader()
        for object in objects:
            csvwriter.writerow(brickset.dict(object))

def open_csv(filename, object):
    global brickset
    fieldnames = sorted(brickset.dict(object).keys())
    csvfile = open(filename, 'wb')
    csvwriter = unicodecsv.DictWriter(csvfile, dialect=unicodecsv.excel,
                                  fieldnames=fieldnames,
                                  quoting=unicodecsv.QUOTE_NONNUMERIC)
    csvwriter.writeheader()
    return csvfile, csvwriter

def append_csv(csvwriter, objects):
    for object in objects:
        print "\tSet %s [%s]" % (object.name, object.number)
        csvwriter.writerow(brickset.dict(object))

# print brickset
themes = brickset.service.getThemes(apikey)['themes']

csvfile, csvwriter = open_csv("sets.csv", brickset.factory.create('sets'))

for theme in themes:
    print "Getting sets for theme %s" % theme.theme
    sets = brickset.service.getSets(apiKey=apikey, userHash="", query="",
                                    theme=theme.theme, subtheme="",
                                    setNumber="", year="", owned="",
                                    wanted="", orderBy="",
                                    pageSize="1000", pageNumber="1",
                                    userName="")[0]
    append_csv(csvwriter, sets)

csvfile.close()
