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
  paints = 0
  colors = dict()
  inputs = [1]
  runner = runComputer(data, inputs)

  while True:
    color = next(runner, 'exhausted!')
    turn = next(runner, 'exhausted!')
    if color == 'exhausted!': break

    if (x,y) not in colors: paints += 1

    if color == 1 or (x,y) in colors:
      colors[(x,y)] = color

    if turn == 0: # left turn
      if direction == U: direction = L
      elif direction == R: direction = U
      elif direction == D: direction = R
      elif direction == L: direction = D
    elif turn == 1: # right turn
      if direction == U: direction = R
      elif direction == R: direction = D
      elif direction == D: direction = L
      elif direction == L: direction = U

    if direction == U: y -= 1
    if direction == R: x += 1
    if direction == D: y += 1
    if direction == L: x -= 1

    maxy = max(maxy, y)
    maxx = max(maxx, x)
    miny = min(miny, y)
    minx = min(minx, x)

    inputs.append(0 if (x,y) not in colors else colors[(x,y)])

  print(paints)

  x, y = 0, 0
  for y in range(miny, maxy + 1):
    line = ""
    for x in range(minx, maxx + 1):
      line += "█" if (x,y) in colors and colors[(x,y)] == 1 else '░'
    print(line)

  return 'Done!'

print(solve(data))