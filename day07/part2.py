import itertools
import collections

with open('input.txt', 'r') as file:
  data = list(map(int, file.read().splitlines()[0].split(",")))

class Computer:
  def __init__(self, program):
    self.i = 0
    self.lastOutput = None
    self.halted = False
    self.program = program.copy()

  def run(self, input):
    if self.halted:
      raise RuntimeError("Computer was halted already")
    i, output = runComputer(self.program, self.i, input)
    self.i = i
    self.halted = self.halted or output is None
    self.lastOutput = output
    return output

def runComputer(program, i, input):
  while True:
    opcode = program[i] % 100

    if opcode == 99:
      return (i, None)

    mode1 = (program[i] - opcode) // 100 % 10
    mode2 = (program[i] - opcode) // 1000 % 10

    param1 = program[i+1] if mode1 == 1 else program[program[i+1]]
    
    if opcode in [1, 2, 5, 6, 7, 8]:
      param2 = program[i+2] if mode2 == 1 else program[program[i+2]]

    if opcode == 1: # add
      param3 = program[i+3]
      program[param3] = param1 + param2
      i += 4

    elif opcode == 2: # mul
      param3 = program[i+3]
      program[param3] = param1 * param2
      i += 4
    
    elif opcode == 3: # mov
      param1 = program[i+1]
      program[param1] = input
      i += 2

    elif opcode == 4: # out
      output = param1
      i += 2
      return (i, output)

    elif opcode == 5: # jump-if-true
      i = param2 if param1 != 0 else i+3

    elif opcode == 6: # jump-if-false
      i = param2 if param1 == 0 else i+3

    elif opcode == 7: # less-than
      param3 = program[i+3]
      program[param3] = 1 if param1 < param2 else 0
      i += 4

    elif opcode == 8: # equals
      param3 = program[i+3]
      program[param3] = 1 if param1 == param2 else 0
      i += 4

    else:
      raise ValueError(f'opcode {opcode} from {program[i]}')
  
  raise ValueError(f'input {input} escaped the loop!')

def solve(input):
  results = collections.OrderedDict()

  # for seq in [(9,7,8,5,6)]: # itertools.permutations(range(5, 10), 5):
  for seq in itertools.permutations(range(5, 10), 5):
    # print('trying seq', seq)

    computers = list()

    for phase in seq:
      computer = Computer(data)
      _output = computer.run(phase) # initialize with phase
      computers.append(computer)

    computers[4].lastOutput = 0 # simulate that E gives A 0 the first time
    running = True

    while running:
      running = False
      for n in range(0, 5):
        if computers[n].halted: continue
        input = computers[(n - 1 + 5) % 5].lastOutput
        # print(n, input)
        computers[n].run(input)
        running = True
      if not computers[4].halted:
        results[seq] = computers[4].lastOutput

    # for c in computers: print(c.halted)

  # for x in results: print(x, results[x])

  maxKey = max(results.keys(), key=(lambda k: results[k]))
  return maxKey, results[maxKey], 'and', (9,7,8,5,6), results[(9,7,8,5,6)]

print(solve(data))