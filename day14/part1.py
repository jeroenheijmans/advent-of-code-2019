from math import ceil
from collections import defaultdict

with open('input.txt', 'r') as file:
  data = file.read().splitlines()
  reactions = dict()
  for line in data:
    parts = line.split(" => ")
    inputs = []
    for i in parts[0].split(","):
      spl = i.split()
      inputs.append((int(spl[0]), spl[1].strip()))
    outparts = parts[1].strip().split()
    output = (int(outparts[0]), outparts[1])
    reactions[output] = inputs

def solve(data):
  print('REACTIONS:')
  for k in reactions:
    print(k, reactions[k])
  print()

  needed = { "FUEL": 1 }
  leftovers = defaultdict(int)
  limit = 0

  while True and limit < 1000:
    limit += 1
    print("Need:", needed, '--- leftovers:', dict(leftovers))

    if len(needed) == 1 and "ORE" in needed:
      print("\nFOUND NEEDS!")
      break

    newneeded = dict()

    if "ORE" in needed:
      newneeded["ORE"] = needed["ORE"]
    
    for n in needed:
      for rkey in reactions:
        if rkey[1] == n:
          produced = rkey[0]
          factor = int(ceil(needed[n] / produced))
          ingredients = reactions[rkey]
          surplus = (produced * factor) - needed[n]
          leftovers[n] += surplus

          if n in leftovers and leftovers[n] >= needed[n]:
            leftovers[n] -= needed[n]
          else:
            for ing in ingredients:
              alreadyneeded = 0 if ing[1] not in newneeded else newneeded[ing[1]]
              req = ing[0] * factor
              print(ing, 'at factor', factor)
              newneeded[ing[1]] = req + alreadyneeded

    needed = newneeded
  
  return needed

# Not 85902 ("too low")
print(solve(reactions))