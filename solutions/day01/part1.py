with open('input.txt', 'r') as file:
  data = file.read().splitlines()

sum = 0

for line in data: 
  sum += int(line) // 3 - 2

print(sum)