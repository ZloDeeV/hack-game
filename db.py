from pymongo import MongoClient
from geojson import importBuildings
import settings

def getDB():
  client = MongoClient(
      'mongodb://{}'.format(settings.DB_STRING))
  return client['hack-game']

def importGeo():
  db = getDB()
  db.buildings.insert_many(importBuildings('export.geojson'))

def testGeo():
  db = getDB()
  query = {
    'loc': {
      '$near': [32.049544, 54.780151],
      '$maxDistance': 0.001
    }
  }
  for doc in db.buildings.find(query).limit(100):
    print(doc)
