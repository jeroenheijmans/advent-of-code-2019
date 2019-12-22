from time import time
from itertools import permutations, combinations

with open('input.txt', 'r') as file:
  data = list(file.read().splitlines())

def energy(vector):
  return abs(vector[0]) + abs(vector[1]) + abs(vector[2])

def energies(vectors):
  return sum(map(energy, vectors))

def total(positions, velocities):
  return sum([energy(positions[i]) * energy(velocities[i])  for i in range(4)])
    

def solve(input):
  # Example 1 (Expected: 2772)
  positions = [(-1, 0, 2), (2, -10, -7), (4, -8, 8), (3, 5, -1)]

  # Example 2 (expected: 4_686_774_924)
  positions = [(-8, -10, 0), (5, 5, 10), (2, -7, 3), (9, -8, -3)]

  # My input (expected: puzzle answer :D)
  positions = [(-8, -9,  -7), (-5,  2,  -1), (11,  8, -14), ( 1, -4, -11)]

  # Made up example (expected: 168)
  # positions = [(0,0,0), (1,0,0), (0,2,0), (3,4,5)]

  velocities = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
  start = time()
  startpositions = positions.copy()
  startvelocities = velocities.copy()
  combis = [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]

  for step in range(1, 4_686_774_924 + 16_000_000_000):
    vchanges = [(0,0,0), (0,0,0), (0,0,0), (0,0,0)]

    for one, two in combis:
      p1 = positions[one]
      p2 = positions[two]

      dx = 1 if p1[0] < p2[0] else -1 if p1[0] > p2[0] else 0
      dy = 1 if p1[1] < p2[1] else -1 if p1[1] > p2[1] else 0
      dz = 1 if p1[2] < p2[2] else -1 if p1[2] > p2[2] else 0

      vc1 = vchanges[one]
      vc2 = vchanges[two]
      vchanges[one] = (vc1[0] + dx, vc1[1] + dy, vc1[2] + dz)
      vchanges[two] = (vc2[0] - dx, vc2[1] - dy, vc2[2] - dz)

    for one in range(4):
      vc1 = vchanges[one]
      p1 = positions[one]
      v1 = velocities[one]
      velocities[one] = (v1[0] + vc1[0], v1[1] + vc1[1], v1[2] + vc1[2])
      v1 = velocities[one]
      positions[one] = (
        p1[0] + v1[0],
        p1[1] + v1[1],
        p1[2] + v1[2]
      )
    
    if positions == startpositions and velocities == startvelocities:
      print("step", step, "time", str(round(time() - start, 4)).ljust(6, "0"), positions)
      print("\npositions: ", positions)
      print("velocities:", velocities, "\n")
      break

    if step % 1e6 == 0:
      print("step", step, "time", str(round(time() - start, 4)).ljust(6, "0"), positions)

  return step

# Not 209373549846 (guessed after running the brute force version (see branch) for 91805.5432 seconds :O - not good...)
print("Part 2:", solve(data))
