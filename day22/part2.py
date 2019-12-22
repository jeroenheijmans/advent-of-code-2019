from time import time

def deckstring(deck):
  return " ".join([str(n) for n in deck])

def solve(data, size):
  decks = set()
  step = 0
  start = time()
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

  while True:
    if step % 10 == 0: print(f"Step {step} time {str(round(time() - start, 4))}")

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
    
    step += 1
    txt = deckstring(deck)
    if txt in decks: break
    decks.add(txt)

  print("Repeating at", step)

  return deck[2020] if size > 2020 else None

with open('input.txt', 'r') as file:
  raw = file.read().splitlines()

print("Solution:", solve(raw, 10007))