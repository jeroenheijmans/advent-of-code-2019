from collections import defaultdict

def firstten(freqs):
  return ''.join(list(map(str, freqs))[:10])

def solve(input):
  freqs = data.copy()
  pattern = [0, 1, 0, -1]
  maxlength = len(freqs)

  for _ in range(100):
    newfreqs = []

    for i in range(maxlength):
      # line = ""
      newf = 0
      j = 0
      for j in range(maxlength):
        repeats = i + 1
        pidx = (j + 1) // repeats
        pidx = pidx % 4
        factor = pattern[pidx]
        newf += freqs[j] * factor
        
        # line += f"{freqs[j]}*{str(factor).ljust(2, ' ')} + "
      # line += f"= {abs(newf) % 10} ({newf})"
      # print(line)
      newfreqs.append(abs(newf) % 10)
    
    freqs = newfreqs
  
  return firstten(freqs)


with open('input.txt', 'r') as file:
  data = list(map(int, file.read().splitlines()[0]))

# Not 3469461657
print("Part 1:", solve(data))
