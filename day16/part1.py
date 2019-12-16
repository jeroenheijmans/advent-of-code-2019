from collections import defaultdict

def solve(input):
  return None

with open('input.txt', 'r') as file:
  data = list(map(int, file.read().splitlines()[0].split(",")))

print("Part 1:", solve(data))