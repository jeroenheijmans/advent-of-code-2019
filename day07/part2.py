import itertools
import collections

with open('input.txt', 'r') as file:
  data = list(map(int, file.read().splitlines()[0].split(",")))

class Computer:
  def __init__(self, program):
    self.i = 0
    self.program = program.copy()

  def run(self, input):
    i, output = self.__run(self.i, input)
    self.i = i
    return output

  def __run(self, i, input):
    program = self.program

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

  for seq in itertools.permutations(range(5, 10), 5):
    print('trying seq', seq)

    computers = list()

    for phase in seq:
      computer = Computer(data)
      _output = computer.run(phase) # initialize with phase
      computers.append(computer)

    amplification = 0
    running = True

    while running:
      for computer in computers:
        output = computer.run(amplification)
        if output is None:
          running = False
          break
        amplification = output
    
    results[seq] = amplification

  # for x in results: print(x, results[x])

  return max(results.values())

print(solve(data))