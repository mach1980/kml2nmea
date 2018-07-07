from fastkml import kml
from shapely.geometry import Point, LineString, Polygon

data = open('test.kml', 'rt', encoding="utf-8")
doc = data.read().encode('utf-8')
k = kml.KML()
k.from_string(doc)

print(k.to_string(prettyprint=True))
#features = list(k.features())
#print ("features:" + str(len(features)))
