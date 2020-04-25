from flask import Flask, request
from bson.json_util import dumps
from bson.objectid import ObjectId
from db import getDB
from flask_cors import CORS

app = Flask('hack-game')
CORS(app)
db = getDB()

def testGame(props, value):
  return not props

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/walk', methods=['GET'])
def walk():
  lon = request.args.get('lon')
  lat = request.args.get('lat')
  try:
    query = {
      'loc': {
        '$near': [float(lon), float(lat)],
        '$maxDistance': 0.003
      }
    }
    buildings = db.buildings.find(query).limit(100)
    return dumps(buildings)
  except ValueError:
    return 'Неверные координаты', 500


@app.route('/hack', methods=['GET', 'POST'])
def hack():
  obj_id = request.args.get('id')
  query = { '_id': ObjectId(obj_id)}
  building = db.buildings.find_one(query)
  if request.method == 'GET':
    return dumps(building)
  else:
    return testGame(building.get('game_properties'), request.args.get('value'))


@app.errorhandler(404)
def page_not_found(e):
  return 'Not found', 404

app.run()
