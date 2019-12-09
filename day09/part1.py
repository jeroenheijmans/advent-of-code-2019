with open('input.txt', 'r') as file:
  data = list(map(int, file.read().splitlines()[0].split(",")))

def runComputer(data, phase, input):
  program = data.copy()
  output = None
  i = 0
  hasUsedPhase = False

  while True:
    opcode = program[i] % 100

    if opcode == 99:
      break

    mode1 = (program[i] - opcode) // 100 % 10
    mode2 = (program[i] - opcode) // 1000 % 10

    param1 = program[i+1] if mode1 == 1 or opcode == 3 else program[program[i+1]]
    param2 = (program[i+2] if mode2 == 1 else program[program[i+2]]) if opcode in [1, 2, 5, 6, 7, 8] else None
    param3 = program[i+3] if opcode in [1, 2, 7, 8] else None

    if opcode == 1: # add
      program[param3] = param1 + param2
      i += 4

    elif opcode == 2: # mul
      program[param3] = param1 * param2
      i += 4
    
    elif opcode == 3: # mov
      program[param1] = input if hasUsedPhase else phase
      hasUsedPhase = True
      i += 2

    elif opcode == 4: # out
      output = param1
      i += 2

    elif opcode == 5: # jump-if-true
      i = param2 if param1 != 0 else i+3

    elif opcode == 6: # jump-if-false
      i = param2 if param1 == 0 else i+3

    elif opcode == 7: # less-than
      program[param3] = 1 if param1 < param2 else 0
      i += 4

    elif opcode == 8: # equals
      program[param3] = 1 if param1 == param2 else 0
      i += 4

    else:
      raise ValueError(f'opcode {opcode} from {program[i]}')
  
  if output is None:
    raise ValueError(f'input {input} resulted in no output')

  return output

def solve(data):

  return 'No solution found'

print(solve(data))
