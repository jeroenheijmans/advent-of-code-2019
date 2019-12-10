import math

with open('input.txt', 'r') as file:
  data = list(file.read().splitlines())

def solve(input):
  points = dict()
  x, y = -1, -1

  for line in input:
    y += 1
    x = -1
    for char in line:
      x += 1
      if char == "#":
        points[(x,y)] = dict()
  
  for p in points.keys():
    for other in points.keys():
      if p == other: continue
      rad = math.atan2(other[1]-p[1], other[0]-p[0])
      key = int(rad * 100000) + 1
      if key not in points[p]:
        points[p][key] = list()
      points[p][key].append(other)
    #print(p, points[p], len(points[p]))

  result = max(points, key = lambda p: len(points[p].values()))

  return result, ' visible: ', len(points[result].values())

print(solve(data))