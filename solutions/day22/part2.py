def reverse(position, size):
  return size - position - 1

def increment(position, size, n):
  return (n * position) % size

def reverseIncrement(target, size, n):
  return pow(n, -1, size) * target % size

def cut(position, size, n):
  return position - n if position >= n else size - (n - position)

def reverseCut(target, size, n):
  return cut(target, size, -n) % size

def solve(data, size, times, target):
  num = lambda line: int(''.join(filter(lambda x: x.isdigit() or x == "-", line)))
  program = [
    (1, None) if "stack" in line else
    (2, num(line)) if "inc" in line else
    (3, num(line)) if "cut" in line else
    None # Problem!
    for line in data
  ]

  backwards = list(reversed(program))
  position = target

  for i in range(times):
    if i % 1e4 == 0: print(f"Reversed complete shuffles: {i}")

    for op in backwards:
      if op[0] == 1: position = reverse(position, size)
      elif op[0] == 2: position = reverseIncrement(position, size, op[1])
      elif op[0] == 3: position = reverseCut(position, size, op[1])

  return position

with open('input.txt', 'r') as file:
  raw = file.read().splitlines()

decksize = 119_315_717_514_047 # Prime number, does that mean something?
shuffles = 101_741_582_076_661 # Prime number as well, does it mean anything?

part1 = solve(raw, size = 10007, times = 1, target = 2939)
print("\nVerify part 1, should be 2019, is:", part1, "\n")

part2 = solve(raw, size = decksize, times = shuffles, target = 2020)
print("Solution:", part2)