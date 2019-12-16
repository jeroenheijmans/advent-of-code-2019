from collections import defaultdict

def firsteight(freqs):
  return ''.join(list(map(str, freqs))[:8])

def solve(input):
  messageoffset = int(input[:7])
  freqs = list(map(int, input))
  pattern = [0, 1, 0, -1]
  maxlength = len(freqs)

  for step in range(100):
    print(step)
    newfreqs = []

    for i in range(maxlength):
      print('  -', i)
      newf = 0
      repeats = i + 1
      for j in range(maxlength):
        pidx = (j + 1) // repeats
        pidx = pidx % 4
        factor = pattern[pidx]
        newf += freqs[j] * factor
        
      newfreqs.append(abs(newf) % 10)
    
    freqs = newfreqs
  
  return firsteight(freqs[:messageoffset])


with open('input.txt', 'r') as file:
  txt = file.read().splitlines()[0]

print("Part 2:", solve(txt * 10000))
