from itertools import permutations

with open('input.txt', 'r') as file:
  data = list(file.read().splitlines())

def solve(input):
  positions = [(-8, -9,  -7), (-5,  2,  -1), (11,  8, -14), ( 1, -4, -11)]
  velocities = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]

  for _ in range(1000):
    for one, two in permutations([0, 1, 2, 3], 2):
      v1 = velocities[one]
      p1 = positions[one]
      p2 = positions[two]

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

  energy = 0

  for one in range(4):
    pot = abs(positions[one][0]) + abs(positions[one][1]) + abs(positions[one][2])
    kin = abs(velocities[one][0]) + abs(velocities[one][1]) + abs(velocities[one][2])
    total = pot * kin
    energy += total

  return energy

print(solve(data))
