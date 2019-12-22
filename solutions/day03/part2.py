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
      if (x, y) not in points:
        points[(x, y)] = cost
  return points

def solve(input):
  points1 = lineToTupleSet(input[0])
  points2 = lineToTupleSet(input[1])
  crossings = set(points1.keys()) & set(points2.keys())
  return min(map(lambda p: points1[p] + points2[p], crossings))

print(solve(data))