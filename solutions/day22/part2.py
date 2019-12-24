def num(line):
  return int(''.join(filter(lambda x: x.isdigit() or x == "-", line)))

def rev(position, size):
  return size - position - 1

def inc(position, size, n):
  return (n * position) % size

def revinc(target, size, n):
  # Dumb implementation for now
  for i in range(size):
    result = inc(i, size, n)
    if result == target: return i

def cut(position, size, n):
  return position - n if position >= n else size - (n - position)

def revcut(target, size, n):
  return cut(target, size, -n) % size

print("TESTS:")
print("revinc works if: 0 ==", revinc(0, 10, 3))
print("revinc works if: 7 ==", revinc(1, 10, 3))
print("revinc works if: 4 ==", revinc(2, 10, 3))
print("revinc works if: 1 ==", revinc(3, 10, 3))
print("revinc works if: 8 ==", revinc(4, 10, 3))
print("revinc works if: 5 ==", revinc(5, 10, 3))
print("revinc works if: 2 ==", revinc(6, 10, 3))
print("revinc works if: 9 ==", revinc(7, 10, 3))
print("revinc works if: 6 ==", revinc(8, 10, 3))
print("revinc works if: 3 ==", revinc(9, 10, 3))
print("revinc works if: 8685 ==", revinc(9806, 10007, 38))
print()


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
  r = []

  for i in range(times):
    for op in backwards:
      if op[0] == 1: position = rev(position, size)
      elif op[0] == 2: position = revinc(position, size, op[1])
      elif op[0] == 3: position = revcut(position, size, op[1])
      r.append(position)
    
    print(list(reversed(r)))
    return position

  return "Answer not found"

with open('input.txt', 'r') as file:
  raw = file.read().splitlines()

decksize = 119_315_717_514_047 # Prime number, does that mean something?
shuffles = 101_741_582_076_661 # Prime number as well, does it mean anything?

part1 = solve(raw, size = 10007, times = shuffles, target = 2939)
print("\nVerify part 1, should be 2019, is:", part1, "\n")

# Not 67591732435243 (too high)
# part2 = solve(raw, size = decksize, times = shuffles, target = 2020)
# print("Solution:", part2)