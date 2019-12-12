from itertools import combinations

with open('input.txt', 'r') as file:
  data = list(file.read().splitlines())

def solve(input):
  # Example 1

  # Example 2
  # positions = [
  #   (-8, -10, 0),
  #   (5, 5, 10),
  #   (2, -7, 3),
  #   (9, -8, 3)
  # ]

  positions = [
    (-8, -9,  -7),
    (-5,  2,  -1),
    (11,  8, -14),
    ( 1, -4, -11)
  ]

  velocities = [
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0)
  ]

  for step in range(1000):
    for one in range(len(positions)):
      for two in range(len(positions)):
        if one == two: continue
        velocities[one] = (
          (1 if positions[one][0] < positions[two][0] else (-1 if positions[one][0] > positions[two][0] else 0)),
          (1 if positions[one][1] < positions[two][1] else (-1 if positions[one][1] > positions[two][1] else 0)),
          (1 if positions[one][2] < positions[two][2] else (-1 if positions[one][2] > positions[two][2] else 0))
        )

    for one in range(len(positions)):
      positions[one] = (
        positions[one][0] + velocities[one][0],
        positions[one][1] + velocities[one][1],
        positions[one][2] + velocities[one][2]
      )

    print(step, '=', positions)

  energy = 0

  for one in range(len(positions)):
    pot = positions[one][0] + positions[one][1] + positions[one][2]
    kin = velocities[one][0] + velocities[one][1] + velocities[one][2]
    total = pot * kin
    energy += total

  return energy

# Not 35889
# Not -7
print(solve(data))
