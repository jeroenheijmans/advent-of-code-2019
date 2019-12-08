with open('input.txt', 'r') as file:
  data = list(map(int, file.read().splitlines()[0]))

def solve(data):
  width = 6
  height = 25

  matrix = [[2 for x in range(width)] for y in range(height)]

  size = height * width
  nr = len(data) // size
  i = 0

  for _ in range(nr):
    for w in range(height):
      for h in range(width):
        if matrix[w][h] == 2 and data[i] < 2:
          matrix[w][h] = data[i]
        i += 1

  for h in range(width):
    line = ""
    for w in range(height):
      if matrix[w][h] == 0: line += '·' # black
      if matrix[w][h] == 1: line += '█' # white
      if matrix[w][h] == 2: line += ' ' # transparent
    
    print(line)

  return 'finished'

print(solve(data))