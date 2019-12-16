from time import time
from collections import defaultdict

def firsteight(freqs):
  return ''.join(list(map(str, freqs))[:8])

officialRepeatCount = 10000

def solve(data, messageRepeat = officialRepeatCount):
  messageoffset = int(data[:7]) % len(data)
  freqs = list(map(int, data))
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
  
  return firsteight(freqs[messageoffset:])

with open('input.txt', 'r') as file:
  txt = file.read().splitlines()[0]

# 43852383 wrong, too high!
print("Part 2:", solve(txt))
