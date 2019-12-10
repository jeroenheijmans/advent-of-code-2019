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
      key = int(math.degrees(rad))
      
      if key not in points[p]:
        points[p][key] = list()
      points[p][key].append(other)
    
  station = max(points, key = lambda p: len(points[p].values()))

  for p in points.keys():
    for key in points[p].keys():
      points[p][key].sort(key = lambda p2: abs(p[0] - p2[0]) + abs(p[1] - p2[1]))

  print('station at', station)
  for x in sorted(points[station].keys()): print(x, ' => ', points[station][x])

  i = 0
  printed = True
  while i < 200 and printed:
    printed = False
    for key in sorted(points[station].keys(), reverse=True):
      if len(points[station][key]) == 0: continue
      i += 1
      target = points[station][key].pop(0)
      result = target[0] * 100 + target[1]
      print(i, 'zapping', target, 'result would be', result)
      printed = True
      if i == 200: break

  return 'done'

# Not 315
print(solve(data))