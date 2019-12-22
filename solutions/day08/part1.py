from collections import defaultdict

with open('input.txt', 'r') as file:
  data = list(map(int, file.read().splitlines()[0]))

def solve(data):
  width, height = 25, 6
  i = 0
  checksums = {}

  while i < len(data):
    colors = defaultdict(lambda: 0)
    for _ in range(width * height):
      colors[data[i]] += 1
      i += 1
    checksums[colors[0]] = colors[1] * colors[2]

  return checksums[min(checksums.keys())]

print(solve(data))