import os
from time import time
from collections import defaultdict

# Windows only :P
clear = lambda: os.system('cls')

def firsteight(freqs):
  return ''.join(list(map(str, freqs))[:8])

officialRepeatCount = 10000

def draw(freqs):
  clear()
  maxlen = len(freqs)
  buffer = ""
  width = 60
  full = False
  for n in range(width * width):
    if n >= maxlen:
      full = True
      break
    if n % width == 0: buffer += "\n"
    buffer += " " + str(freqs[n])
  if not full: buffer = buffer[:-7] + " ...etc"
  
  print(buffer)


def solve(data, messageRepeat = 3):
  messageoffset = 0 # int(data[:7])
  freqs = list(map(int, data)) * messageRepeat
  pattern = [0, 1, 0, -1]
  maxlength = len(freqs)
  start = time()

  for step in range(100):
    draw(freqs)
    print()
    print('step', str(step).ljust(2, ' '), 'time', str(round(time() - start, 4)).ljust(7, "0"))
    # print("press enter to continue")
    # input()

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
