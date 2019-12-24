from collections import deque, defaultdict

def runComputer(data, inputqueue: deque, inputDefault = lambda: -1):
  program = defaultdict(int, { k: v for k, v in enumerate(data) })
  output = None
  i = 0
  relbase = 0

  while True:
    opcode = program[i] % 100

    if opcode == 99: break

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

    if opcode == 1: # addition
      program[p3] = program[p1] + program[p2]
      i += 4
    elif opcode == 2: # multiplication
      program[p3] = program[p1] * program[p2]
      i += 4
    elif opcode == 3: # input
      if len(inputqueue) > 0:
        program[p1] = inputqueue.popleft()
        i += 2
      else:
        program[p1] = inputDefault()
        i += 2
        yield "CONTINUE"
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

def solve(data):
  # q = deque()
  # vm = runComputer(data, q)

  # while True:
  #   status = next(vm, "HALTED")
  #   if status == "HALTED": break

  return "No solution found yet"

with open('input.txt', 'r') as file:
  raw = list(map(int, file.read().splitlines()[0].split(",")))

print("Solution:", solve(raw))