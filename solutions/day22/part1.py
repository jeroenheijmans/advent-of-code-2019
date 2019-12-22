def num(line):
  return int(''.join(filter(lambda x: x.isdigit() or x == "-", line)))

def rev(position, size):
  return size - position - 1

def inc(position, size, n):
  return (n * position) % size

def cut(position, size, n):
  return position - n if position >= n else size - (n - position)

def solve(data, size):
  program = [
    (1, None) if "stack" in line else
    (2, num(line)) if "inc" in line else
    (3, num(line)) if "cut" in line else
    None # Problem!
    for line in data
  ]

  position = 2019

  for op in program:
    if op[0] == 1: position = rev(position, size)
    elif op[0] == 2: position = inc(position, size, op[1])
    elif op[0] == 3: position = cut(position, size, op[1])

  return position

with open('input.txt', 'r') as file:
  raw = file.read().splitlines()

print("Solution:", solve(raw, 10007))