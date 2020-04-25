import json
from geomath import polygonCenter, polygonArea

class Building:
  def __init__(self, raw_data):
    g = raw_data.get('geometry')
    p = raw_data.get('properties')
    self.name = p.get('name')
    self.levels = p.get('building:levels')
    self.self_id = p.get('@id')
    self.loc = polygonCenter(g)
    self.area = polygonArea(g)
    self.game_type = 'bc'
    self.game_properties = {}
    self.street = p.get('addr:street')
    self.housenumber = p.get('addr:housenumber')
    self.difficult = 0

  def toJson(self):
    return json.dumps(self.__dict__)

  def isValid(self):
    return self.street and self.housenumber and self.area > 350

def importBuildings(filename):
  result = []
  with open(filename) as file:
    data = json.load(file)
    buildings = data['features']
    for i in range(len(buildings)):
      building = Building(buildings[i])
      if building.isValid():
        result.append(building.__dict__)
  return result

