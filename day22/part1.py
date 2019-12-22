def rev(position, size):
  return size - position - 1

def inc(position, size, n):
  return (n * position) % size

def cut(position, size, n):
  return position - n if position >= n else size - (n - position)

def solve(data, size):
  program = []
  for line in [x.strip() for x in data]:
    if "deal into new stack" in line:
      program.append((1, None))
    if "deal with increment" in line:
      n = int(line.replace("deal with increment ", ""))
      program.append((2, n))
    if "cut" in line:
      n = int(line.replace("cut ", ""))
      program.append((3, n))

  position = 2019

  for op in program:
    if op[0] == 1: position = rev(position, size)
    elif op[0] == 2: position = inc(position, size, op[1])
    elif op[0] == 3: position = cut(position, size, op[1])

  return position

with open('input.txt', 'r') as file:
  raw = file.read().splitlines()

print("Tests:")
print("rev 0 =?", rev(9, 10))
print("rev 9 =?", rev(0, 10))
print("inc 9 =?", inc(3, 10, 3))
print("inc 2 =?", inc(4, 10, 3))
print("cut 9 =?", cut(2, 10, 3))
print("cut 7 =?", cut(0, 10, 3))
print("cut 4 =?", cut(0, 10, -4))
print("cut 5 =?", cut(1, 10, -4))
print("cut 9 =?", cut(5, 10, -4))
print()
print("Solution:", solve(raw, 10007))