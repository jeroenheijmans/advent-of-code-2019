from collections import defaultdict

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

def draw(level):
  minx = min([x for x, _ in level.keys()])
  miny = min([y for _, y in level.keys()])
  maxx = max([x for x, _ in level.keys()])
  maxy = max([y for _, y in level.keys()])

  buffer = []
  for y in range(miny, maxy+1):
    line = ""
    for x in range(minx, maxx+1):
      line += level[(x,y)] if (x,y) in level else ' '
    buffer.append(line)
  
  with open('temp.txt', 'w', newline='\r\n') as file:
    for line in buffer: 
      print(line)
      file.write(line + "\n")

def findanswer(level):
  miny = min([y for _, y in level.keys()])
  maxy = max([y for _, y in level.keys()])

  for y in range(miny, maxy+1):
    bottomy = y + 10
    xsAtTop    = [p[0] for p in level if level[p] == "#" and p[1] == y ]
    xsAtBottom = [p[0] for p in level if level[p] == "#" and p[1] == bottomy ]

    if len(xsAtTop) == 0 or len(xsAtBottom) == 0:
      continue 

    minx = min(xsAtBottom)
    maxx = max(xsAtTop)
    
    if minx in xsAtTop and maxx in xsAtBottom:
      return minx * 10000 + y

def solve(data):
  x, y = 0, 0
  level = dict()

  spotted = False
  while True:
    if y >= 500:
      break

    # print("Checking", x, y)
    inputs = [y, x] # IntCode requires a stack of commands, not a queue!
    runner = runComputer(data, inputs)

    status = next(runner, 'halt')
    if status == 'halt': break

    if status == 0:
      level[(x,y)] = "."
    elif status == 1:
      level[(x,y)] = "#"
      spotted = True
      x = max([p[0] for p in level if level[p] == "#"])
    
    if (x,y) in level and level[(x,y)] == "." and spotted:
      x = min([p[0] for p in level if p[1] == y and level[p] == "#"])
      y += 1
      spotted = False
    else:
      x += 1

    answer = findanswer(level)
    if answer is not None: return answer

  draw(level)

  return None

with open('input.txt', 'r') as file:
  raw = list(map(int, file.read().splitlines()[0].split(",")))

# Not 1530078, tried to spot it manually in the output :P
# Not 1490076, also guessed by hand :P
# Not 1040050
print("Part 2:", solve(raw))