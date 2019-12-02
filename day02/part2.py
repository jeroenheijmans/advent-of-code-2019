with open('input.txt', 'r') as file:
  data = list(map(int, file.read().splitlines()[0].split(",")))

def solve(input):

  for noun in range(0, 100):
    for verb in range(0, 100):
      program = input.copy()

      program[1] = noun
      program[2] = verb

      i = 0

      while True:
        if program[i] == 1:
          program[program[i+3]] = program[program[i+2]] + program[program[i+1]]
          i += 4
        elif program[i] == 2:
          program[program[i+3]] = program[program[i+2]] * program[program[i+1]]
          i += 4
        elif program[i] == 99:
          break
      
      if program[0] == 19690720:
        return 100 * noun + verb

print(solve(data))