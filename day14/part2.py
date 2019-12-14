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

  inventory = defaultdict(int)
  limit = 0
  inventory["ORE"] = 1000000000000

  while True and limit < 5: # just a few steps...
    print('inventory', dict(inventory))
    limit += 1

    for r in reactions:
      possibleFactors = []
      for ing in reactions[r]:
        factor = 0 if inventory[ing[1]] == 0 else inventory[ing[1]] // ing[0]
        possibleFactors.append(factor)
      finalFactor = min(possibleFactors)

      for ing in reactions[r]:
        inventory[ing[1]] -= finalFactor * ing[0]
      
      print('producing', r, 'factor', finalFactor)
      inventory[r[1]] += r[0] * finalFactor


  return inventory["FUEL"]

print(solve(reactions))