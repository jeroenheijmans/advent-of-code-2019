with open('input.txt', 'r') as file:
  data = file.read().splitlines()

def solve(input):
  entries = list(map(lambda x: (x.split(")")[0], x.split(")")[1]), input))

  orbits = dict()

  for a,b in entries:
    if a in orbits: orbits[a].add(b)
    else: orbits[a] = set([b])
    if b in orbits: orbits[b].add(a)
    else: orbits[b] = set([a])

  # print(orbits)

  keepGoing = True
  loop = 1

  paths = set(["YOU"])

  while keepGoing and loop < 50000:
    keepGoing = False
    loop += 1

    newPaths = paths.copy()

    for path in paths:
      tail = path[-3:]
      for step in orbits[tail]:
        if step not in path:
          newPath = f"{path}{step}"
          # print(newPath)
          if newPath not in newPaths:
            if step == "SAN": print(f"{path}SAN")
            keepGoing = True
            newPaths.add(newPath)

    paths = newPaths

  print('after', loop, 'iterations')
  return paths

result = solve(data)
# print(result)