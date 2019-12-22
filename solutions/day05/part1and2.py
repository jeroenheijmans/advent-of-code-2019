from math import log10

with open('input.txt', 'r') as file:
  data = list(map(int, file.read().splitlines()[0].split(",")))

def solve(data, input):
  program = data.copy()
  output = 'no result found'
  i = 0

  while True:
    opcode = program[i] % 100

    if opcode == 99:
      break

    mode1 = (program[i] - opcode) // 100 % 10
    mode2 = (program[i] - opcode) // 1000 % 10
    # mode3 = (program[i] - opcode) // 10000 % 10 # not used (yet?)

    param1 = program[i+1] if mode1 == 1 else program[program[i+1]]
    
    if opcode in [1, 2, 5, 6, 7, 8]:
      param2 = program[i+2] if mode2 == 1 else program[program[i+2]]

    # add
    if opcode == 1:
      param3 = program[i+3]
      program[param3] = param1 + param2
      i += 4

    # mul
    elif opcode == 2:
      param3 = program[i+3]
      program[param3] = param1 * param2
      i += 4
    
    # mov
    elif opcode == 3:
      param1 = program[i+1]
      program[param1] = input
      i += 2

    # out
    elif opcode == 4:
      output = param1
      i += 2

    # jump-if-true
    elif opcode == 5:
      i = param2 if param1 != 0 else i+3

    # jump-if-false
    elif opcode == 6:
      i = param2 if param1 == 0 else i+3

    # less-than
    elif opcode == 7:
      param3 = program[i+3]
      program[param3] = 1 if param1 < param2 else 0
      i += 4

    # equals
    elif opcode == 8:
      param3 = program[i+3]
      program[param3] = 1 if param1 == param2 else 0
      i += 4

    else:
      raise ValueError(f'opcode {opcode} from {program[i]}')
  
  return output

print('part1', solve(data, 1))
print('part2', solve(data, 5))
