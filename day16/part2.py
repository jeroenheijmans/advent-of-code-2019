from time import time
from collections import defaultdict

def firsteight(freqs):
  return ''.join(list(map(str, freqs))[:8])

officialRepeatCount = 10000

def solve(data, messageRepeat = 1):
  messageoffset = 0 # int(data[:7])
  freqs = list(map(int, data)) * messageRepeat
  pattern = [0, 1, 0, -1]
  maxlength = len(freqs)
  start = time()

  for step in range(100):
    print('step', str(step).ljust(2, ' '), 'time', str(round(time() - start, 4)).ljust(7, "0"))
    newfreqs = []

    for i in range(maxlength):
      newFrequency = 0
      j = 0
      repeats = i + 1
      for j in range(repeats - 1, maxlength):
        pidx = (j + 1) // repeats
        pidx = pidx % 4
        factor = pattern[pidx]
        newFrequency += freqs[j] * factor
        
      newfreqs.append(abs(newFrequency) % 10)
    
    freqs = newfreqs
  
  return firsteight(freqs[messageoffset:])

with open('input.txt', 'r') as file:
  txt = file.read().splitlines()[0]

# 43852383 wrong, too high!
print("Part 2:", solve(txt))
