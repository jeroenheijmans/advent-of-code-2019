def reverse(position, size):
  return size - position - 1

def increment(position, size, n):
  return (n * position) % size

def reverseIncrement(target, size, n):
  return pow(n, -1, size) * target % size

def cut(position, size, n):
  return position - n if position >= n else size - (n - position)

def reverseCut(target, size, n):
  return cut(target, size, -n) % size

def solve(data, size, times, target):
  # num = lambda line: int(''.join(filter(lambda x: x.isdigit() or x == "-", line)))
  # program = [
  #   (1, None) if "stack" in line else
  #   (2, num(line)) if "inc" in line else
  #   (3, num(line)) if "cut" in line else
  #   None # Problem!
  #   for line in data
  # ]

  # This is how far cards are "drawn apart" (with some Excel magic and 
  # adhoc code, for my input). I guess basically this is what my input
  # boils down to.
  stepsize = 74911153708239
  # So the above could also be calculated by doing a few cards of the
  # deck just 1 step, and then see how much they "move".

  # So "careful not to overflow" was the actual hint that would make this
  # operation harder, when in Python one does not overflow, I guess!?
  position = (target + (stepsize * (decksize - times))) % decksize

  # backwards = list(reversed(program))
  # position = target
  # for i in range(times):
  #   previous = position
  #   for op in backwards:
  #     if op[0] == 1: position = reverse(position, size)
  #     elif op[0] == 2: position = reverseIncrement(position, size, op[1])
  #     elif op[0] == 3: position = reverseCut(position, size, op[1])

  return position

with open('input.txt', 'r') as file:
  raw = file.read().splitlines()

decksize = 119315717514047 # Prime number, does that mean something?
shuffles = 101_741_582_076_661 # Prime number as well, does it mean anything?

# part1 = solve(raw, size = decksize, times = 1, target = 2939)
# print("\nVerify part 1, should be 2019, is:", part1, "\n")

# Not 117599454398659
# Not 107116967390935 (assuming a recurrance size of 3828, part 2 would be 2221 shuffles in)
# Not 67317446177430 (assuming recurrance size of 1042, remainder would be 1027 shuffles backwards)
# Not 100578495860738 (first guess after using apparent increases of 74911153708239)
# Not 56173932054930 (second guess after trying to correct parts of the answer)
part2 = solve(raw, size = decksize, times = shuffles, target = 0)
print("Solution:", part2)