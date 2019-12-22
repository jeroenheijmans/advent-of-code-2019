def deckstring(deck):
  return " ".join([str(n) for n in deck])

def solve(data, size, times):
  my2020s = []
  step = 0
  deck = list(range(size))

  program = []
  for line in [x.strip() for x in data]:
    if "deal into new stack" in line:
      program.append((1, None))
    if "deal with increment" in line:
      n = int(line.replace("deal with increment ", ""))
      program.append((2, n))
    if "cut" in line:
      n = int(line.replace("cut ", ""))
      program.append((3, n))

  for i in range(times):
    for op in program:
      n = op[1]

      if op[0] == 1:
        deck.reverse()
      
      if op[0] == 2:
        newdeck = [0] * size
        for i in range(size):
          newdeck[(i*n) % size] = deck[i]
        deck = newdeck
      
      if op[0] == 3:
        deck = deck[n:] + deck[:n]

  print("At step", step, "it is", my2020s)

  return deck[2020] if size > 2020 else None

with open('input.txt', 'r') as file:
  raw = file.read().splitlines()

print("Solution:", solve(raw, size = 119_315_717_514_047, times = 101_741_582_076_661))