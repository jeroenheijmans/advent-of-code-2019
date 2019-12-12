from time import time
from itertools import permutations

with open('input.txt', 'r') as file:
  data = list(file.read().splitlines())

def solve(input):
  # Example 2
  positions = [(-8, -10, 0), (5, 5, 10), (2, -7, 3), (9, -8, -3)]

  # My input:
  positions = [(-8, -9,  -7), (-5,  2,  -1), (11,  8, -14), ( 1, -4, -11)]
  velocities = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]

  start = time()

  for step in range(4686774924 + 1):
    if step % 1e5 == 0: print(step, time() - start)
    print
    # maxStepsAtOnce = 1e9

    for one, two in permutations([0, 1, 2, 3], 2):
      v1 = velocities[one]
      p1 = positions[one]
      p2 = positions[two]

      # totaldx = p1[0] - p2[0]
      # totaldy = p1[1] - p2[1]
      # totaldz = p1[2] - p2[2]

      dx = 1 if p1[0] < p2[0] else -1 if p1[0] > p2[0] else 0
      dy = 1 if p1[1] < p2[1] else -1 if p1[1] > p2[1] else 0
      dz = 1 if p1[2] < p2[2] else -1 if p1[2] > p2[2] else 0

      velocities[one] = (v1[0] + dx, v1[1] + dy, v1[2] + dz)

    for one in range(4):
      p1 = positions[one]
      v1 = velocities[one]
      positions[one] = (
        p1[0] + v1[0],
        p1[1] + v1[1],
        p1[2] + v1[2]
      )

  return step

print(solve(data))
