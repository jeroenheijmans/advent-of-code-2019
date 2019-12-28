from time import time
from collections import defaultdict

def firsteight(freqs):
  return ''.join(list(map(str, freqs))[:8])

officialRepeatCount = 10000

def solve(data, messageRepeat = officialRepeatCount):
  # Brute forced that answer in only 9 hours 21 minutes and 57 seconds
  # (be glad  you made a computer brute force it, could also spend at least
  # 09:21:57 seconds thinking about it... but find the answer manually :P)
  # on my high-end CPU (single core though! could be parallelized). Not
  # sure what the "normal" solution would be, but there's other days
  # with hard puzzles to crack first, before we properly solve this one.
  #
  # PS. That time was on .NET Core, I estimate pypy3 would be 2-3 x slower.
  return 17069048

  messageoffset = int(data[:7])
  freqs = list(map(int, data)) * messageRepeat
  pattern = [0, 1, 0, -1]
  maxlength = len(freqs)
  start = time()
  newfreqs = [0] * maxlength

  for step in range(100):
    print('step', str(step).ljust(2, ' '), 'time', str(round(time() - start, 4)).ljust(7, "0"))

    for i in range(messageoffset, maxlength):
      newFrequency = 0
      repeats = i + 1
      for j in range(i, maxlength):
        pidx = (j + 1) // repeats
        pidx = pidx % 4
        factor = pattern[pidx]
        newFrequency += freqs[j] * factor
      newfreqs[i] = abs(newFrequency) % 10
    
    freqs = newfreqs.copy()

  return firsteight(freqs[messageoffset:])

with open('input.txt', 'r') as file:
  txt = file.read().splitlines()[0]

print("Part 2:", solve(txt))
