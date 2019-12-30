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

  print("Careful, this will be sloooowww")

  results = []

  for position in range(size):
    if position % 100 == 0: print(position)
    line = [position]
    for _ in range(size):
      for op in program:
        if op[0] == 1: position = rev(position, size)
        elif op[0] == 2: position = inc(position, size, op[1])
        elif op[0] == 3: position = cut(position, size, op[1])
      line.append(position)
    results.append(line)

  with open("temp.txt", "w") as file:
    i = 0
    for line in results:
      print("Writing line", i)
      i+=1
      for p in line:
        file.write(str(p))
        file.write("\t")
      file.write("\n")

  return position

with open('input.txt', 'r') as file:
  raw = file.read().splitlines()

solve(raw, 10007)
print("See temp.txt")
