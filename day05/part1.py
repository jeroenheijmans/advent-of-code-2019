from math import log10

with open('input.txt', 'r') as file:
  data = list(map(int, file.read().splitlines()[0].split(",")))

def solve(program, input):
  output = 'none'
  counter = 0
  i = 0

  while True: # safety... and counter < 10000:
    counter += 1

    opcode = program[i] % 100
    mode1 = (program[i] - opcode) // 100 % 10
    mode2 = (program[i] - opcode) // 1000 % 10
    # mode3 = (program[i] - opcode) // 10000 % 10

    # add
    if opcode == 1:
      param1 = program[i+1] if mode1 == 1 else program[program[i+1]]
      param2 = program[i+2] if mode2 == 1 else program[program[i+2]]
      param3 = program[i+3]
      program[param3] = param1 + param2
      i += 4

    # mul
    elif opcode == 2:
      param1 = program[i+1] if mode1 == 1 else program[program[i+1]]
      param2 = program[i+2] if mode2 == 1 else program[program[i+2]]
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
      param1 = program[i+1] if mode1 == 1 else program[program[i+1]]
      output = param1
      i += 2

    elif opcode == 99:
      print(program[i], 'halt')
      break

    else:
      raise ValueError(f'opcode {opcode} from {program[i]}')
  
  return output

input = 1
print(solve(data, input))
