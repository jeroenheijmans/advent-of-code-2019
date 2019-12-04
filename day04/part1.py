with open('input.txt', 'r') as file:
  data = file.read().splitlines()

def solve(input):
  data = input[0].split("-")
  lower = int(data[0])
  upper = int(data[1])
  n = 0

  for x in range(lower, upper + 1):
    candidate = str(x)
    okay = True
    for i in range(len(candidate) - 1):
      if candidate[i] == candidate[i + 1]:
        okay = False
        break
      if candidate[i] > candidate[i + 1]:
        okay = False
        break
    if okay: n += 1

  return n

# Not 8
print(solve(data))