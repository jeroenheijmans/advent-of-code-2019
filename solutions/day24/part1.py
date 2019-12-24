def draw(level):
  size = 5 # assume a square
  for y in range(size):
    line = "".join([level[(x,y)] for x in range(size)])
    print(line)

def stringify(level):
  return "".join(level.values())

def neighbors(level, p):
  return [p for p in [
    (p[0] - 1, p[1]),
    (p[0] + 1, p[1]),
    (p[0], p[1] - 1),
    (p[0], p[1] + 1),
  ] if p in level]

def solve(raw):
  level = dict()

  x,y = 0,0
  for line in raw:
    for c in line:
      level[(x,y)] = c
      x += 1
    y += 1
    x = 0
  
  layouts = set()

  while True:
    draw(level)
    # input()

    txt = stringify(level)
    if txt in layouts: break
    layouts.add(txt)
    newlevel = dict()
    for p in level:
      ns = neighbors(level, p)
      bugcount = sum([1 for n in ns if level[n] == "#"])
      if level[p] == "#" and not bugcount == 1: newlevel[p] = "."
      elif level[p] == "." and (bugcount == 1 or bugcount == 2): newlevel[p] = "#"
      else: newlevel[p] = level[p]
    level = newlevel

  power = 1
  result = 0
  for p in level:
    if level[p] == "#": result += power
    power = power * 2

  return result

with open('input.txt', 'r') as file:
  raw = file.read().splitlines()

# Not 33423330 :'()
print("Solution:", solve(raw))