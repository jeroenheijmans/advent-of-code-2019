import os
import readchar
from collections import defaultdict

# Windows only :P
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

N, S, W, E, QUIT, AUTO = 1, 2, 3, 4, -1, -2
WALL, OK, GOAL = 0, 1, 2
opposites = { N: S, S: N, E: W, W: E }

dxs = { N: 0, S: 0, W: -1, E: 1 }
dys = { N: -1, S: 1, W: 0, E: 0 }

controls = { 'j': W, 'i': N, 'l': E, 'k': S, 'q': QUIT, 'a': AUTO }

def draw(walls, space, pos, goal):
  clear()
  for y in range(-30, 30):
    line = ""
    for x in range(-30, 30):
      if (x,y) == (0,0): line += 'S'
      elif (x,y) == goal: line += 'X'
      elif (x,y) in walls: line += '█'
      elif (x,y) == pos: line += 'D'
      elif (x,y) in space: line += '·'
      else: line += '░'
    print(line)
  print("At position", pos)

def readmove():
  move = QUIT
  while move < 0:
    print("Please provide input")
    i = readchar.readchar().decode('utf-8')
    print(i)
    if i in controls:
      move = controls[i]
      break
  return move

def solve(data):
  inputs = []
  runner = runComputer(data, inputs)
  x, y = 0, 0
  goal = None
  walls = set()
  space = set([(0,0)])
  exhausted = set([(0,0)])
  mode = 0

  while True:
    counter = 0
    for m in [N,E,S,W]:
      inputs.append(m)
      status = next(runner, 'halt')

      x += dxs[m]
      y += dys[m]

      if status == WALL:
        counter += 1
        walls.add((x, y))
        x -= dxs[m]
        y -= dys[m]
      elif status == OK:
        space.add((x,y))
        m = opposites[m]
        x += dxs[m]
        y += dys[m]
        inputs.append(m)
        _ = next(runner, 'halt')
      elif status == GOAL:
        goal = (x,y)
        m = opposites[m]
        x += dxs[m]
        y += dys[m]
        inputs.append(m)
        _ = next(runner, 'halt')
        draw(walls, space, (x, y), goal)

    if counter == 3:
      exhausted.add((x,y))

    if mode == 0:
      opts = {
        W: (x - 1, y),
        N: (x, y - 1),
        E: (x + 1, y),
        S: (x, y + 1),
      }

      candidates = [c for c in opts if opts[c] not in exhausted and opts[c] not in walls]
      if len(candidates) == 1:
        exhausted.add(opts[candidates[0]])
      draw(walls, space, (x, y), goal)
      print(candidates)
      move = candidates[0]

    if mode == 1:
      draw(walls, space, (x, y), goal)
      move = readmove()

    if move == QUIT:
      break
    if move == AUTO:
      mode = 0
      continue

    inputs.append(move)
    status = next(runner, 'halt')
    if status == 'halt': break

    x += dxs[move]
    y += dys[move]

    if status == WALL:
      walls.add((x, y))
      x -= dxs[move]
      y -= dys[move]
    elif status == OK:
      space.add((x,y))
    elif status == GOAL:
      draw(walls, space, (x, y), goal)
      print('GOAL!')
      mode = 1

  return "Spaces encountered", len(space)

print(solve(data))
