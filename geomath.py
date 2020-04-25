from math import pi, fabs, sin

RADIUS = 6378137

def rad(num):
  return num * pi / 180

def centroid(polygon):
  x_sum = 0
  y_sum = 0
  length = 0
  for point in polygon:
    x_sum += point[0]
    y_sum += point[1]
    length += 1
  return [x_sum / length, y_sum / length]

def area(coords):
  total = 0
  if coords and len(coords) > 0:
    total += fabs(ringArea(coords[0]))
    for i in range(1, len(coords) - 1):
      total -= fabs(ringArea(coords[i]))

  return total

def ringArea(coords):
  coordsLength = len(coords)
  total = 0
  p1 = None
  p2 = None
  p3 = None
  lowerIndex = 0
  middleIndex = 0
  upperIndex = 0

  if (coordsLength > 2):
    for i in range(coordsLength):
      if i == coordsLength - 2:
        lowerIndex = coordsLength - 2
        middleIndex = coordsLength - 1
        upperIndex = 0
      elif i == coordsLength - 1:
        lowerIndex = coordsLength - 1
        middleIndex = 0
        upperIndex = 1
      else:
        lowerIndex = i
        middleIndex = i + 1
        upperIndex = i + 2

      p1 = coords[lowerIndex]
      p2 = coords[middleIndex]
      p3 = coords[upperIndex]
      total += (rad(p3[0]) - rad(p1[0])) * sin(rad(p2[1]))

    total = total * RADIUS * RADIUS / 2
  return total

def polygonCenter(geojson_geometry):
  if geojson_geometry.get('type') == 'Polygon':
    coords = geojson_geometry.get('coordinates')
    return centroid(coords[0])

  else:
    return []

def polygonArea(geojson_geometry):
  if geojson_geometry.get('type') == 'Polygon':
    coords = geojson_geometry.get('coordinates')
    return area(coords)

  else:
    return 0

def checkCoords(lon, lat):
  return 180 > fabs(lon) > 0 and 180 > fabs(lat) > 0
