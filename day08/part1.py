with open('input.txt', 'r') as file:
  data = list(map(int, file.read().splitlines()[0]))

def solve(data):
  # matrix = [[-1 for x in range(w)] for y in range(h)]

  size = 25 * 6
  nr = len(data) // size
  i = 0
  lowest = None

  for layer in range(nr):
    nr1 = 0
    nr2 = 0
    for _ in range(size):
      if data[i] == 1: nr1 += 1
      if data[i] == 2: nr2 += 1
      i += 1

    checksum = nr1 * nr2
    lowest = checksum if lowest is None else min(lowest, checksum)
    print(layer, checksum)
    

  return 'found', lowest

# no 774
print(solve(data))