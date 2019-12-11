from collections import defaultdict

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

U = 0
R = 1
D = 2
L = 3

def solve(data):
  direction = U
  x, y = 0, 0
  maxy, maxx, miny, minx = 0, 0, 0, 0
  whites = set()
  painteds = set()
  inputs = [0]
  runner = runComputer(data, inputs)

  while True:
    color = next(runner, 'exhausted!')
    turn = next(runner, 'exhausted!')
    if color == 'exhausted!': break

    if color == 1:
      painteds.add((x, y))
      whites.add((x, y))
    if color == 0:
      if (x, y) in whites: whites.remove((x, y))

    if turn == 0: # left turn
      if direction == U: direction = L
      if direction == R: direction = U
      if direction == D: direction = R
      if direction == L: direction = D
    if turn == 1: # right turn
      if direction == U: direction = R
      if direction == R: direction = D
      if direction == D: direction = L
      if direction == L: direction = U

    if direction == U: y -= 1
    if direction == R: x += 1
    if direction == D: y += 1
    if direction == L: x -= 1

    maxy = max(maxy, y)
    maxx = max(maxx, x)
    miny = min(miny, y)
    minx = min(minx, x)

    inputs.append(1 if (x,y) in whites else 0)
    print(len(painteds))

  x, y = 0, 0
  for y in range(miny, maxy):
    line = ""
    for x in range(minx, maxx):
      line += "█" if (x, y) in whites else '░'
    # print(line)

  return 'Done!'

# Not 7068
# Not 7634
# Not 6263
# Not 184
# Not 5785
print(solve(data))