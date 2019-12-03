with open('input.txt', 'r') as file:
  data = file.read().splitlines()

def lineToTupleSet(line):
  points = {}
  cost = 0
  x = 0
  y = 0
  for instruction in line.split(","):
    direction = instruction[0]
    length = int(instruction[1:])
    for _ in range(0, length):
      cost += 1
      if direction == "U": y -= 1
      if direction == "R": x += 1
      if direction == "D": y += 1
      if direction == "L": x -= 1
      point = tuple([x, y])
      if point not in points:
        points[point] = cost
  return points

def distance(p1):
  return abs(p1[0]) + abs(p1[1])

def solve(input):
  points1 = lineToTupleSet(input[0])
  points2 = lineToTupleSet(input[1])
  crossings = set(points1.keys()).intersection(set(points2.keys()))
  lowestCost = 10000000
  for p in crossings:
    cost = points1[p] + points2[p]
    lowestCost = min([lowestCost, cost])
  return lowestCost

print(solve(data))