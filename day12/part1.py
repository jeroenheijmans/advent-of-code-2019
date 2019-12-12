from itertools import combinations

with open('input.txt', 'r') as file:
  data = list(file.read().splitlines())

def solve(input):
  # Example 1
  positions = [
    (-1, 0, 2),
    (2, -10, -7),
    (4, -8, 8),
    (3, 5, -1)
  ]

  # Example 2
  positions = [
    (-8, -10, 0),
    (5, 5, 10),
    (2, -7, 3),
    (9, -8, -3)
  ]
  
  # Own example
  # positions = [
  #   (1, 0, 0),
  #   (0, 0, 0),
  #   (0, 0, 0),
  #   (0, 0, 0)
  # ]

  # My input:
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

    print(
      step,
      '=',
      list(map(lambda p: (str(p[0]).rjust(3), str(p[1]).rjust(3), str(p[2]).rjust(3)), positions)),
      'vel',
      list(map(lambda p: (str(p[0]).rjust(3), str(p[1]).rjust(3), str(p[2]).rjust(3)), velocities)),
    )

    for one in range(len(positions)):
      for two in range(len(positions)):
        if one == two: continue

        if positions[one][0] < positions[two][0]: dx = 1
        elif positions[one][0] > positions[two][0]: dx = -1
        else: dx = 0
        
        if positions[one][1] < positions[two][1]: dy = 1
        elif positions[one][1] > positions[two][1]: dy = -1
        else: dy = 0
        
        # if one == 0: print(positions[one][2], 'vs', positions[two][2])
        if positions[one][2] < positions[two][2]: dz = 1
        elif positions[one][2] > positions[two][2]: dz = -1
        else: dz = 0

        velocities[one] = (
          velocities[one][0] + dx,
          velocities[one][1] + dy,
          velocities[one][2] + dz
        )
        # if one == 0: print(velocities[one])

    for one in range(len(positions)):
      positions[one] = (
        positions[one][0] + velocities[one][0],
        positions[one][1] + velocities[one][1],
        positions[one][2] + velocities[one][2]
      )

  energy = 0

  for one in range(len(positions)):
    pot = abs(positions[one][0]) + abs(positions[one][1]) + abs(positions[one][2])
    kin = abs(velocities[one][0]) + abs(velocities[one][1]) + abs(velocities[one][2])
    total = pot * kin
    energy += total
    # print(pot, '*', kin, '=', total)

  return energy

# Not 35889
# Not -7
# Not -2789
# Not 623
print(solve(data))
