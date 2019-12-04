with open('input.txt', 'r') as file:
  data = file.read().splitlines()

def solve(input):
  lower, upper = map(int, input[0].split("-"))
  n = 0

  for x in range(lower, upper):
    candidate = str(x)
    twosame = False
    increases = True
    length = len(candidate)
    
    for i in range(1, length):
      if candidate[i] == candidate[i - 1]:
        # maybe twosame...
        invalid1 = i > 1 and candidate[i] == candidate[i - 2]
        invalid2 = i < length - 1 and candidate[i] == candidate[i + 1]
        if not invalid1 and not invalid2:
          twosame = True
        
      if candidate[i] < candidate[i - 1]:
        increases = False
        break

    if twosame and increases:
      n += 1

  return n

# Not 251
print(solve(data))