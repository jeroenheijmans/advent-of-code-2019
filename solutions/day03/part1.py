with open('input.txt', 'r') as file:
  data = file.read().splitlines()

def lineToTupleSet(line):
  points = set()
  x = 0
  y = 0
  for instruction in line.split(","):
    direction = instruction[0]
    length = int(instruction[1:])
    for _ in range(0, length):
      if direction == "U": y -= 1
      if direction == "R": x += 1
      if direction == "D": y += 1
      if direction == "L": x -= 1
      points.add((x, y))
  return points

def distance(p1, p2 = (0, 0)):
  return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def solve(input):
  points1 = lineToTupleSet(input[0])
  points2 = lineToTupleSet(input[1])
  crossings = points1 & points2
  return min(map(distance, crossings))

print(solve(data))