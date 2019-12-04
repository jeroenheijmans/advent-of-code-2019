with open('input.txt', 'r') as file:
  data = file.read().splitlines()

def solve(input):
  data = input[0].split("-")
  lower = int(data[0])
  upper = int(data[1])
  n = 0

  for x in range(lower, upper):
    candidate = str(x)
    twosame = False
    increases = True
    for i in range(1, len(candidate) - 1):
      if candidate[i] == candidate[i - 1]:
        twosame = True
      if candidate[i] < candidate[i - 1]:
        increases = False
        break
    if twosame and increases:
      print(candidate)
      n += 1

  return n

# Not 8
# Not 78876
# Not 78850
# Not 4980
print(solve(data))