from collections import defaultdict

with open('input.txt', 'r') as file:
  data = list(map(int, file.read().splitlines()[0]))

def solve(data):
  width = 25
  height = 6
  i = 0
  checksums = {}

  while i < len(data):
    colors = defaultdict(lambda: 0)
    for _ in range(width * height):
      colors[data[i]] += 1
      i += 1
    checksums[colors[0]] = colors[1] * colors[2]

  return checksums[sorted(checksums.keys())[0]]

print(solve(data))