def num(line):
  return int(''.join(filter(lambda x: x.isdigit() or x == "-", line)))

def rev(position, size):
  return size - position - 1

def revrev(target, size):
  return rev(target, size) # same thing :)

def inc(position, size, n):
  return (n * position) % size

def revinc(target, size, n):
  return size - (target * (size // n) % size)

def cut(position, size, n):
  return position - n if position >= n else size - (n - position)

def revcut(target, size, n):
  return cut(target, size, -n) % size

print("Tests:")
print("revinc 0 =?", revinc(0, 10, 3))
print("revinc 7 =?", revinc(1, 10, 3))
print("revinc 4 =?", revinc(2, 10, 3))
print("revinc 1 =?", revinc(3, 10, 3))
print("revinc 8 =?", revinc(4, 10, 3))
print("revinc 5 =?", revinc(5, 10, 3))
print("revinc 2 =?", revinc(6, 10, 3))
print("revinc 9 =?", revinc(7, 10, 3))
print("revinc 6 =?", revinc(8, 10, 3))
print("revinc 3 =?", revinc(9, 10, 3))
print()
print("revcut 3 =?", revcut(0, 10, 3))
print("revcut 4 =?", revcut(1, 10, 3))
print("revcut 5 =?", revcut(2, 10, 3))
print("revcut 6 =?", revcut(3, 10, 3))
print("revcut 7 =?", revcut(4, 10, 3))
print("revcut 8 =?", revcut(5, 10, 3))
print("revcut 9 =?", revcut(6, 10, 3))
print("revcut 0 =?", revcut(7, 10, 3))
print("revcut 1 =?", revcut(8, 10, 3))
print("revcut 2 =?", revcut(9, 10, 3))

def solve(data, size, times, target):
  program = [
    (1, None) if "stack" in line else
    (2, num(line)) if "inc" in line else
    (3, num(line)) if "cut" in line else
    None # Problem!
    for line in data
  ]

  backwards = reversed(program)

  position = target
  for i in reversed(range(times)):
    for op in backwards:
      if op[0] == 1: position = revrev(position, size)
      elif op[0] == 2: position = revinc(position, size, op[1])
      elif op[0] == 3: position = revcut(position, size, op[1])
    
    print(f"At {i} card ending up at 2020 came from {position}")

  return "Answer not found"

with open('input.txt', 'r') as file:
  raw = file.read().splitlines()

# Not 67591732435243 (too high)
part2 = solve(raw, size = 119_315_717_514_047, times = 101_741_582_076_661, target = 2020)
print("Solution:", part2)