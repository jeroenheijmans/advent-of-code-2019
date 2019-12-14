from math import ceil, floor
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

def solveFor(reactions, fuelNeeded):
  needed = { "FUEL": fuelNeeded }
  leftovers = defaultdict(int)

  while True:
    if len(needed) == 1 and "ORE" in needed:
      break

    newneeded = dict()

    if "ORE" in needed:
      newneeded["ORE"] = needed["ORE"]
    
    for n in needed:
      for rkey in reactions:
        if rkey[1] == n:
          actuallyneeded = max(0, needed[n] - leftovers[n])
          leftovers[n] -= (needed[n] - actuallyneeded)
          if actuallyneeded == 0:
            continue

          produced = rkey[0]
          factor = int(ceil(actuallyneeded / produced))
          ingredients = reactions[rkey]
          surplus = (produced * factor) - actuallyneeded
          leftovers[n] += surplus

          for ing in ingredients:
            alreadyneeded = 0 if ing[1] not in newneeded else newneeded[ing[1]]
            req = ing[0] * factor
            newneeded[ing[1]] = req + alreadyneeded

    needed = newneeded
  
  return needed

def solve(reactions):
  trillion = 1_000_000_000_000
  fuel = 1
  tried = set()

  while True:
    tried.add(fuel)
    needed = solveFor(reactions, fuel)
    ore = needed["ORE"]
    if ore > trillion: break
    fuel = floor(fuel * trillion / ore)
    if fuel in tried: break

  return fuel

# Could well be a lucky answer though, off-by-one for other inputs..
print("Part 2:", solve(reactions))