from collections import defaultdict

with open('input.txt', 'r') as file:
  data = list(map(int, file.read().splitlines()[0].split(",")))

ops = {
  1: 'ADD',
  2: 'MUL',
  3: 'INP',
  4: 'OUT',
  5: 'JIT',
  6: 'JIF',
  7: 'LES',
  8: 'EQU',
  9: 'REL'
}

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

    param1, param2, param3 = None, None, None

    if mode1 == 0: param1 = program[program[i+1]] # position
    elif mode1 == 1: param1 = program[i+1] # immediate
    elif mode1 == 2: param1 = program[program[i+1] + relbase] # relative

    if opcode in [1, 2, 5, 6, 7, 8]:
      if mode2 == 0: param2 = program[program[i+2]]
      elif mode2 == 1: param2 = program[i+2]
      elif mode2 == 2: param2 = program[program[i+2] + relbase]
    
    if opcode in [1, 2, 7, 8]:
      if mode3 == 0: param3 = program[i+3]
      elif mode3 == 1: param3 = program[i+3]
      elif mode3 == 2: param3 = program[program[i+3] + relbase]

    #print()
    #print(program.values())
    #print('operation', opcode, ops[opcode], ' - at', i, 'relbase', relbase, ' - output', output)
    #print('  modes', mode1, mode2, mode3)
    #print('  params', param1, param2, param3)
    
    # print(opcode, ops[opcode], '- i: ', str(i).rjust(3, ' '), '- relbase:', str(relbase).rjust(4, ' '), '- modes', mode1, mode2, mode3, ' - params', param1, param2, param3)

    if opcode == 1: # add
      if mode3 == 2: param3 = program[i+3] + relbase
      program[param3] = param1 + param2
      i += 4

    elif opcode == 2: # mul
      if mode3 == 2: param3 = program[i+3] + relbase
      program[param3] = param1 * param2
      i += 4
    
    elif opcode == 3: # input
      if mode1 == 2: param1 = program[i+1] + relbase
      program[param1] = input
      i += 2

    elif opcode == 4: # out
      output = param1
      i += 2

    elif opcode == 5: # jump-if-true
      i = param2 if param1 != 0 else i+3

    elif opcode == 6: # jump-if-false
      i = param2 if param1 == 0 else i+3

    elif opcode == 7: # less-than
      if mode3 == 2: param3 = program[i+3] + relbase
      program[param3] = 1 if param1 < param2 else 0
      i += 4

    elif opcode == 8: # equals
      if mode3 == 2: param3 = program[i+3] + relbase
      program[param3] = 1 if param1 == param2 else 0
      i += 4

    elif opcode == 9: # relbase
      relbase += param1
      i += 2

    else:
      raise ValueError(f'opcode {opcode} from {program[i]}')
  
  if output is None:
    raise ValueError(f'input {input} resulted in no output')

  # print(program.values())

  return output

def solve(data):
  part1 = runComputer(data, 1)
  part2 = runComputer(data, 2)
  return 'part1: ', part1, 'and part2: ', part2

print(solve(data))
