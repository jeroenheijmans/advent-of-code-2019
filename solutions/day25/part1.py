from itertools import combinations
from collections import deque, defaultdict
import os

# Windows only :P
clear = lambda: os.system('cls')

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

def command(q, cmd):
  q.extend([ord(c) for c in cmd])
  q.append(10)

def solve(data):
  baseplan = deque([
    "north",
    "west",
    "take mug",
    "west",
    "take easter egg",
    "east",
    "east",
    "south",
    "inv", # Hull Breach [mug, easter egg]

    "south",
    "take asterisk",
    "south",
    "west",
    "north",
    "take jam",
    "south",
    "east",
    "north",
    "inv", # Gift Wrapping Center [..., asterisk, jam]

    "east",
    "take klein bottle",
    "south",
    "west",
    "take tambourine",
    "west",
    "take cake",
    "east",
    "inv", # Navigation [..., tambourine, cake]

    "south",
    "east",
    "take polygon",
    "north",
  ])
  
  items = ["polygon", "easter egg", "tambourine", "asterisk", "mug", "jam", "klein bottle", "cake" ]

  for size in range(4, 9):
    for combi in list(combinations(items, size)):
      print(combi)
      q = deque()
      vm = runComputer(data, q)
      buffer = ""
      plan = baseplan.copy()
      verbose = False
      allowinteractive = False
      done = False
      
      backup = deque([f"drop {w}" for w in items if w not in combi])
      backup.append("east")

      while True:
        status = next(vm, "HALTED")
        if status == "HALTED":
          if done: return "Answer above"
          break

        if status == 10:
          if "robotic voice" in buffer and not ("lighter" in buffer or "heavier" in buffer):
            verbose = True
            done = True
          if verbose: print(buffer)
          if buffer == "Command?":
            if not plan:
              if not backup:
                if allowinteractive:
                  txt = input()
                  command(q, txt)
                else:
                  break
              else:
                txt = backup.popleft()
                command(q, txt)
                if verbose: print(txt)
            else:
              txt = plan.popleft()
              command(q, txt)
          buffer = ""
        else:
          buffer += chr(status)

  return "No solution found yet"

with open('input.txt', 'r') as file:
  raw = list(map(int, file.read().splitlines()[0].split(",")))

print("Solution:", solve(raw))