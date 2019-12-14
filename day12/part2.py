from time import time
from itertools import permutations, combinations

with open('input.txt', 'r') as file:
  data = list(file.read().splitlines())

def energy(vector):
  return abs(vector[0]) + abs(vector[1]) + abs(vector[2])

def energies(vectors):
  return sum(map(energy, vectors))

def solve(input):
  # Example 1
  positions = [(-1, 0, 2), (2, -10, -7), (4, -8, 8), (3, 5, -1)]

  # Example 2
  positions = [(-8, -10, 0), (5, 5, 10), (2, -7, 3), (9, -8, -3)]

  # My input:
  positions = [(-8, -9,  -7), (-5,  2,  -1), (11,  8, -14), ( 1, -4, -11)]

  velocities = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
  start = time()
  startpositions = positions.copy()
  startvelocities = velocities.copy()
  combis = [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]

  for step in range(4_686_774_924 + 16_000_000_000):
    for one, two in combis:
      p1 = positions[one]
      p2 = positions[two]
      v1 = velocities[one]
      v2 = velocities[two]

      dx = 1 if p1[0] < p2[0] else -1 if p1[0] > p2[0] else 0
      dy = 1 if p1[1] < p2[1] else -1 if p1[1] > p2[1] else 0
      dz = 1 if p1[2] < p2[2] else -1 if p1[2] > p2[2] else 0

      velocities[one] = (v1[0] + dx, v1[1] + dy, v1[2] + dz)
      velocities[two] = (v2[0] - dx, v2[1] - dy, v2[2] - dz)

    for one in range(4):
      p1 = positions[one]
      v1 = velocities[one]
      positions[one] = (
        p1[0] + v1[0],
        p1[1] + v1[1],
        p1[2] + v1[2]
      )
    
    if positions == startpositions and velocities == startvelocities:
      print('same!', round(time() - start, 4))
      print(positions)
      print(velocities)
      break

    if step % 1e6 == 0:
      print(step, ",", round(time() - start, 4), positions)

  return step + 1

print(solve(data))
