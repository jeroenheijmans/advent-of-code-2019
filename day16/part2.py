from collections import defaultdict

def firsteight(freqs):
  return ''.join(list(map(str, freqs))[:8])

officialRepeatCount = 10000

def solve(data, messageRepeat = officialRepeatCount):
  data = data * messageRepeat
  messageoffset = int(data[:7])
  freqs = list(map(int, data))
  pattern = [0, 1, 0, -1]
  maxlength = len(freqs)

  for step in range(100):
    if step % 10 == 0: print(step)
    newfreqs = []

    for i in range(maxlength):
      newf = 0
      repeats = i + 1
      for j in range(1):
        pidx = (j + 1) // repeats
        pidx = pidx % 4
        factor = pattern[pidx]
        newf += freqs[j] * factor
        
      newfreqs.append(abs(newf) % 10)
    
    freqs = newfreqs

  print('first 100 digits (full result in file)', ''.join(list(map(str, freqs[:100]))))
  
  with  open('temp.txt', 'w') as file:
    file.write(''.join(list(map(str, freqs))))
  
  return firsteight(freqs[messageoffset:])


with open('input.txt', 'r') as file:
  txt = file.read().splitlines()[0]

# 55555555 wrong, too high (guessed based on output middle section)
print("Part 2:", solve(txt))
