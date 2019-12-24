def draw(levels):
  mini = min(levels.keys())
  maxi = max(levels.keys())

  for i in range(mini, maxi + 1):
    print("\nLevel", i)
    level = levels[i]
    size = 5 # assume a square
    for y in range(size):
      line = "".join([level[(x,y)] for x in range(size)])
      print(line)

def neighbors(levels, rec, p):
  ns = []

  if (p[0] - 1, p[1]) != (2,2) and (p[0] - 1, p[1]) in levels[rec]: ns.append(levels[rec][(p[0] - 1, p[1])])
  if (p[0] + 1, p[1]) != (2,2) and (p[0] + 1, p[1]) in levels[rec]: ns.append(levels[rec][(p[0] + 1, p[1])])
  if (p[0], p[1] - 1) != (2,2) and (p[0], p[1] - 1) in levels[rec]: ns.append(levels[rec][(p[0], p[1] - 1)])
  if (p[0], p[1] + 1) != (2,2) and (p[0], p[1] + 1) in levels[rec]: ns.append(levels[rec][(p[0], p[1] + 1)])

  if rec + 1 in levels:
    if p[1] == 0: ns.append(levels[rec + 1][(2,1)]) # add 8 to A-E
    if p[1] == 4: ns.append(levels[rec + 1][(2,3)]) # add 18 to U-Y
    if p[0] == 0: ns.append(levels[rec + 1][(1,2)]) # add 12 to A/F/K/P/U
    if p[0] == 4: ns.append(levels[rec + 1][(3,2)]) # add 14 to E/J/O/T/Y

  if rec - 1 in levels:
    if p == (2,1): ns.extend([levels[rec - 1][p] for p in levels[rec - 1] if p[1] == 0]) # add toprow to H
    if p == (1,2): ns.extend([levels[rec - 1][p] for p in levels[rec - 1] if p[0] == 0]) # add leftrow to L
    if p == (3,2): ns.extend([levels[rec - 1][p] for p in levels[rec - 1] if p[0] == 4]) # add right to N
    if p == (2,3): ns.extend([levels[rec - 1][p] for p in levels[rec - 1] if p[0] == 4]) # add botrow to R

  return ns

def createlevel(data):
  level = dict()

  x,y = 0,0
  for line in raw:
    for c in line:
      level[(x,y)] = c
      x += 1
    y += 1
    x = 0

  return level


def solve(raw):
  levels = dict()
  levels[0] = createlevel(raw)
  empty = createlevel(["....."] * 5)
  
  for minutes in range(200):
    print(f"At minute {minutes}")
    newlevels = dict()

    for depth in range(-minutes, minutes+1):

      if depth not in levels:
        levels[depth] = empty.copy()

      level = levels[depth]
      newlevel = dict()
      newlevels[depth] = newlevel

      for p in level:
        ns = neighbors(levels, depth, p)
        bugcount = sum([1 for n in ns if n == "#"])
        if level[p] == "#" and not bugcount == 1: newlevel[p] = "."
        elif level[p] == "." and (bugcount == 1 or bugcount == 2): newlevel[p] = "#"
        else: newlevel[p] = level[p]

    levels = newlevels

    # draw(levels)
    # input()

  # draw(levels)

  result = 0
  for rec in range(min(levels.keys()), max(levels.keys())):
    result += sum([1 for p in levels[rec] if levels[rec][p] == "#"])

  return result

with open('input.txt', 'r') as file:
  raw = file.read().splitlines()

# Not 4133
print("Solution:", solve(raw))