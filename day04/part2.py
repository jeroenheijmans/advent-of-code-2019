with open('input.txt', 'r') as file:
  data = file.read().splitlines()

def solve(input):
  lower, upper = map(int, input[0].split("-"))
  n = 0

  for x in range(lower, upper):
    candidate = str(x)
    twosame = False
    increases = True
    prev = candidate[0]
    samecount = 0
    
    for i in range(1, len(candidate)):
      if candidate[i] != prev:
        if samecount == 1: twosame = True
        samecount = 0
        prev = candidate[i]

      if candidate[i] == prev:
        samecount += 1
        
      if candidate[i] < candidate[i - 1]:
        increases = False
        break

    if twosame and increases:
      n += 1

  return n

# Not 251
print(solve(data))