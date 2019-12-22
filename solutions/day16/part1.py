from collections import defaultdict

def firsteight(freqs):
  return ''.join(list(map(str, freqs))[:8])

def solve(input):
  freqs = data.copy()
  pattern = [0, 1, 0, -1]
  maxlength = len(freqs)

  for _ in range(100):
    newfreqs = []

    for i in range(maxlength):
      newf = 0
      j = 0
      for j in range(maxlength):
        repeats = i + 1
        pidx = (j + 1) // repeats
        pidx = pidx % 4
        factor = pattern[pidx]
        newf += freqs[j] * factor
        
      newfreqs.append(abs(newf) % 10)
    
    freqs = newfreqs
  
  return firsteight(freqs)


with open('input.txt', 'r') as file:
  data = list(map(int, file.read().splitlines()[0]))

print("Part 1:", solve(data))
