from collections import Counter

with open('input.txt', 'r') as file:
  data = file.read().splitlines()

def solve(input):
  lower, upper = map(int, input[0].split("-"))
  n = 0

  for x in range(lower, upper):
    candidate = str(x)
    counts = Counter(candidate)
    twosame = 2 in counts.values()
    increases = list(candidate) == sorted(candidate)
    if twosame and increases: n += 1

  return n

print(solve(data))