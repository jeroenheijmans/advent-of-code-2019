with open('input.txt', 'r') as file:
  data = list(map(int, file.read().splitlines()[0]))

def solve(data):
  width = 25
  height = 6
  i = 0
  matrix = [[2 for x in range(height)] for y in range(width)]

  while i < len(data):
    for h in range(height):
      for w in range(width):
        if matrix[w][h] == 2 and data[i] < 2:
          matrix[w][h] = data[i]
        i += 1

  for h in reversed(range(height)):
    line = ""
    for w in reversed(range(width)):
      if matrix[width - 1 - w][height - 1 - h] == 0: line += '░' # black
      if matrix[width - 1 - w][height - 1 - h] == 1: line += '█' # white
      if matrix[width - 1 - w][height - 1 - h] == 2: line += ' ' # transparent
    print(line)

  return 'read the answer above in ascii art!'

print(solve(data))