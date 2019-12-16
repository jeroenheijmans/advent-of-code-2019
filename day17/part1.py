def solve(data):
  return 'No solution found'

with open('input.txt', 'r') as file:
  raw = file.read().splitlines()[0]

print("Part 1:", solve(raw))