with open('input.txt', 'r') as file:
  data = list(map(int, file.read().splitlines()[0]))

def solve(data):
  width = 25
  height = 6

  matrix = [[2 for x in range(height)] for y in range(width)]

  size = height * width
  nr = len(data) // size
  i = 0

  for _ in range(nr):
    for h in range(height):
      for w in range(width):
        if matrix[w][h] == 2 and data[i] < 2:
          matrix[w][h] = data[i]
        i += 1

  for h in range(height):
    line = ""
    for w in range(width):
      if matrix[width - 1 - w][height - 1 - h] == 0: line += '·' # black
      if matrix[width - 1 - w][height - 1 - h] == 1: line += '█' # white
      if matrix[width - 1 - w][height - 1 - h] == 2: line += ' ' # transparent
    
    print(line)

  return 'answer upside down!'

print(solve(data))