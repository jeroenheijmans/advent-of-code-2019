with open('input.txt', 'r') as file:
  data = list(map(int, file.read().splitlines()[0]))

def solve(data):
  # matrix = [[-1 for x in range(w)] for y in range(h)]

  size = 25 * 6
  nr = len(data) // size
  i = 0
  lowest = None
  minZeros = None

  for layer in range(nr):
    nr1 = 0
    nr2 = 0
    zeros = 0
    for _ in range(size):
      if data[i] == 0: zeros += 1
      if data[i] == 1: nr1 += 1
      if data[i] == 2: nr2 += 1
      i += 1

    checksum = nr1 * nr2
    if minZeros is None or zeros < minZeros:
      lowest = checksum
      minZeros = zeros
      print(i, layer, checksum)
    

  return 'found', lowest

print(solve(data))