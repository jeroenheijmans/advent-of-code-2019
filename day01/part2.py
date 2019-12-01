with open('input.txt', 'r') as file:
  data = file.read().splitlines()

def fuelFor(input):
  output = input // 3 - 2
  return 0 if output <= 0 else output + fuelFor(output)

sum = 0

for line in data: 
  sum += fuelFor(int(line))

print(sum)