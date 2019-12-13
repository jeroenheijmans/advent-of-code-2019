with open('input.txt', 'r') as file:
  data = list(map(int, file.read().splitlines()[0].split(",")))

def solve(data):
  return 'No solution found'

print(solve(data))