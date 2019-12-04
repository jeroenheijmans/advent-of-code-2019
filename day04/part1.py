with open('input.txt', 'r') as file:
  data = file.read().splitlines()

def solve(input):
  data = input[0].split("-")
  lower = int(data[0])
  upper = int(data[1])
  n = 0

  for x in range(lower, upper + 1):
    candidate = str(x)
    twosame = False
    increases = True
    for i in range(len(candidate) - 1):
      if candidate[i] == candidate[i + 1]:
        twosame = True
        break
      if candidate[i] > candidate[i + 1]:
        increases = False
    if twosame and increases: n += 1

  return n

# Not 8
# Not 78876
print(solve(data))