import os
from collections import defaultdict

clear = lambda: os.system('cls')

with open('input.txt', 'r') as file:
  data = list(map(int, file.read().splitlines()[0].split(",")))

def runComputer(data, input):
  program = defaultdict(int, { k: v for k, v in enumerate(data) })
  output = None
  i = 0
  relbase = 0

  while True:
    opcode = program[i] % 100

    if opcode == 99:
      break

    mode1 = (program[i] - opcode) // 100 % 10
    mode2 = (program[i] - opcode) // 1000 % 10
    mode3 = (program[i] - opcode) // 10000 % 10

    p1, p2, p3 = None, None, None

    if mode1 == 0: p1 = program[i + 1]
    elif mode1 == 1: p1 = i + 1
    elif mode1 == 2: p1 = program[i + 1] + relbase

    if mode2 == 0: p2 = program[i + 2]
    elif mode2 == 1: p2 = i + 2
    elif mode2 == 2: p2 = program[i + 2] + relbase
  
    if mode3 == 0: p3 = program[i + 3]
    elif mode3 == 1: raise ValueError('Immediate mode invalid for param 3')
    elif mode3 == 2: p3 = program[i + 3] + relbase

    # print('i =', i, '--- operation', opcode, '--- modes', mode1, mode2, mode3, '--- positions', str(p1).rjust(4, ' '), str(p2).rjust(4, ' '), str(p3).rjust(4, ' '))

    if opcode == 1: # addition
      program[p3] = program[p1] + program[p2]
      i += 4
    elif opcode == 2: # multiplication
      program[p3] = program[p1] * program[p2]
      i += 4
    elif opcode == 3: # input
      program[p1] = input.pop()
      i += 2
    elif opcode == 4: # output
      yield program[p1]
      i += 2
    elif opcode == 5: # jump-if-true
      i = program[p2] if program[p1] != 0 else i + 3
    elif opcode == 6: # jump-if-false
      i = program[p2] if program[p1] == 0 else i + 3
    elif opcode == 7: # less-than
      program[p3] = 1 if program[p1] < program[p2] else 0
      i += 4
    elif opcode == 8: # equals
      program[p3] = 1 if program[p1] == program[p2] else 0
      i += 4
    elif opcode == 9: # relative base adjust
      relbase += program[p1]
      i += 2
    else:
      raise ValueError(f'opcode {opcode} from {program[i]}')

def show(level, i = 0):
  while True:
    print("press enter for next step")
    input()
    clear()
    i += 1
    print(i)

    minx = min([p[0] for p in level])
    maxx = max([p[0] for p in level])
    miny = min([p[1] for p in level])
    maxy = max([p[1] for p in level])

    for y in range(miny, maxy + 1):
      line = ""
      for x in range(minx, maxx + 1):
        if level[(x,y)] == 0: line += '·'
        if level[(x,y)] == 1: line += '█'
        if level[(x,y)] == 2: line += '░'
        if level[(x,y)] == 3: line += 'X'
        if level[(x,y)] == 4: line += 'o'
      print(line)
    yield

def solve(data):
  x, y = 0, 0
  bx, by = 0, 0
  px, py = 0, 0
  xdirection = 0
  inputs = [0]
  score = -1
  level = defaultdict(int)
  data[0] = 2 # free play!
  runner = runComputer(data, inputs)
  shower = show(level)

  while True:
    x, y, tile = next(runner, 'halt'), next(runner, 'halt'), next(runner, 'halt')
    if x == 'halt': break
    level[(x,y)] = tile

    if tile == 3:
      px = x
      py = y

    if tile == 4:
      if x > bx: xdirection = 1
      elif x < bx: xdirection = -1
      else: xdirection == 0
      bx = x
      by = y

    if x == -1:
      score = tile

    if (bx + xdirection) < px and by != py:
      inputs.append(-1)
    elif (bx + xdirection) > px and by != py:
      inputs.append(1)
    elif len(inputs) == 0:
      inputs.append(0)

    if tile == 3: next(shower)

  next(shower)

  return 'Score', score

print(solve(data))