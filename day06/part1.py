with open('input.txt', 'r') as file:
  data = file.read().splitlines()

def solve(input):
  entries = list(map(lambda x: (x.split(")")[0], x.split(")")[1]), input))

  orbits = dict()

  for a,b in entries:
    if a in orbits: orbits[a].add(b)
    else: orbits[a] = set([b])

  keepGoing = True
  loop = 0

  while keepGoing:
    keepGoing = False
    loop += 1
    print(loop)

    for keyA in orbits:
      for val in orbits[keyA].copy():
        if not val in orbits:
          continue
        for candidate in orbits[val]:
          if candidate != val and candidate not in orbits[keyA]:
            keepGoing = True
            orbits[keyA].add(candidate)

  return sum(map(len, orbits.values()))

print(solve(data))