from time import time
from itertools import permutations, combinations

with open('input.txt', 'r') as file:
  data = list(file.read().splitlines())

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

  startpxs = [vec[0] for vec in startpositions]
  startpys = [vec[1] for vec in startpositions]
  startpzs = [vec[2] for vec in startpositions]
  startvxs = [vec[0] for vec in startvelocities]
  startvys = [vec[1] for vec in startvelocities]
  startvzs = [vec[2] for vec in startvelocities]

  xinterval = None
  yinterval = None
  zinterval = None

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

    if xinterval is None and startpxs == [vec[0] for vec in positions] and startvxs == [vec[0] for vec in velocities]:
      xinterval = step
    if yinterval is None and startpys == [vec[1] for vec in positions] and startvys == [vec[1] for vec in velocities]:
      yinterval = step
    if zinterval is None and startpzs == [vec[2] for vec in positions] and startvzs == [vec[2] for vec in velocities]:
      zinterval = step

    if xinterval and yinterval and zinterval:
      print("Found all intervals:", xinterval, yinterval, zinterval)
      biggest = max([xinterval, yinterval, zinterval])
      i = 1
      while True:
        result = i * biggest
        if result % xinterval == 0 and result % yinterval == 0 and result % zinterval == 0:
          return result
        i += 1
        if i % 1e7 == 0:
          print("i", i, "time", str(round(time() - start, 4)).ljust(6, "0"), "no answer found yet")

    if step % 1e6 == 0:
      print("step", step, "time", str(round(time() - start, 4)).ljust(6, "0"), positions)

  return step

print("Part 2:", solve(data))
