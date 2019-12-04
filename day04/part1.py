with open('input.txt', 'r') as file:
  data = file.read().splitlines()

def solve(input):
  lower, upper = map(int, input[0].split("-"))
  n = 0

  for x in range(lower, upper):
    candidate = str(x)
    twosame = False
    increases = True
    
    for i in range(1, len(candidate)):
      if candidate[i] == candidate[i - 1]:
        twosame = True
      if candidate[i] < candidate[i - 1]:
        increases = False
        break
    if twosame and increases:
      n += 1

  return n

print(solve(data))