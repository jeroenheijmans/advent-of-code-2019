def deckstring(deck):
  return " ".join([str(n) for n in deck])

def solve(data, size):
  deck = list(range(size))

  for line in [x.strip() for x in data]:

    if "deal into new stack" in line:
      deck.reverse()
      if size < 20: print(f'reverse _ result {deckstring(deck)}')
    
    if "deal with increment" in line:
      n = int(line.replace("deal with increment ", ""))
      newdeck = [0] * size
      for i in range(size):
        newdeck[(i*n) % size] = deck[i]
      deck = newdeck
      if size < 20: print(f"dealinc {n} result {deckstring(deck)}")
    
    if "cut" in line:
      n = int(line.replace("cut ", ""))
      deck = deck[n:] + deck[:n]
      if size < 20: print(f"cutting {n} result {deckstring(deck)}")

  if size < 20:
    print("Final deck:", deckstring(deck))

  return None if size < 2019 else deck[2020]

with open('input.txt', 'r') as file:
  raw = file.read().splitlines()

# print("Test 0:", solve("""
#   deal into new stack
# """.splitlines(), 10))

print("Test 1:", solve("""
  deal with increment 7
  deal into new stack
  deal into new stack
""".splitlines(), 10))
print("Should be: ", "0 3 6 9 2 5 8 1 4 7\n")

print("Test 2:", solve("""
  cut 6
  deal with increment 7
  deal into new stack
""".splitlines(), 10))
print("Should be: ", "3 0 7 4 1 8 5 2 9 6\n")

print("Test 3:", solve("""
  deal with increment 7
  deal with increment 9
  cut -2
""".splitlines(), 10))
print("Should be: ", "6 3 0 7 4 1 8 5 2 9\n")

# Not 2916
# Not 7168
print("Solution:", solve(raw, 10007))