with open('input.txt', 'r') as file:
  data = list(map(int, file.read().splitlines()[0].split(",")))

def solve(program):
  program[1] = 12
  program[2] = 2
  
  i = 0

  while True:
    if program[i] == 1:
      program[program[i+3]] = program[program[i+2]] + program[program[i+1]]
      i += 4
    elif program[i] == 2:
      program[program[i+3]] = program[program[i+2]] * program[program[i+1]]
      i += 4
    elif program[i] == 99:
      return program[0]

print(solve(data))