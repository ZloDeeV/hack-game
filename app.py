from pymongo import MongoClient
from geojson import importBuildings
import settings

client = MongoClient(
    'mongodb://{}@ds115198.mlab.com:15198/hack-game?retryWrites=false'.format(settings.DB_USER))
db = client['hack-game']

def importGeo():
  db.buildings.insert_many(importBuildings('export.geojson'))


def testGeo():
  query = {
    'loc': {
      '$near': [32.049544, 54.780151],
      '$maxDistance': 0.001
    }
  }
  for doc in db.buildings.find(query).limit(100):
    print(doc)

testGeo()
