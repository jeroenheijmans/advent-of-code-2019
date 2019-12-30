def reverse(position, size):
  return size - position - 1

def increment(position, size, n):
  return (n * position) % size

def cut(position, size, n):
  return position - n if position >= n else size - (n - position)

def solve(data, size, times, target):
  num = lambda line: int(''.join(filter(lambda x: x.isdigit() or x == "-", line)))
  program = [
    (1, None) if "stack" in line else
    (2, num(line)) if "inc" in line else
    (3, num(line)) if "cut" in line else
    None # Problem!
    for line in data
  ]

  samples = [0, 1, 2, 3]
  results = []

  for sample in samples:
    for op in program:
      if op[0] == 1: sample = reverse(sample, size)
      elif op[0] == 2: sample = increment(sample, size, op[1])
      elif op[0] == 3: sample = cut(sample, size, op[1])
    results.append(sample)

  diffs = [
    (results[1] - results[0] + size) % size,
    (results[2] - results[1] + size) % size,
    (results[3] - results[2] + size) % size,
  ]

  assert diffs[0] == diffs[1]
  assert diffs[1] == diffs[2]

  stepsize = diffs[0]

  # So "careful not to overflow" was the actual hint that would make this
  # operation harder, when in Python one does not overflow, I guess!?
  position = (target + (stepsize * (decksize - times))) % decksize

  print("THIS IS LIKELY NOT YET THE ANSWER, WE STILL NEED TO PIVOTTTT THE SOLUTION!")

  return position

with open('input.txt', 'r') as file:
  raw = file.read().splitlines()

decksize = 119_315_717_514_047 # Prime number :D
shuffles = 101_741_582_076_661 # Prime number :D

# Not 117599454398659
# Not 107116967390935 (assuming a recurrance size of 3828, part 2 would be 2221 shuffles in)
# Not 67317446177430 (assuming recurrance size of 1042, remainder would be 1027 shuffles backwards)
# Not 100578495860738 (first guess after using apparent increases of 74911153708239)
# Not 56173932054930 (second guess after trying to correct parts of the answer)
# Not 40620801226632 (third guess after trying to tweak the actual calculation in mild despair)
# Not 40620801228652 (fourth guess ... as expected :P)
part2 = solve(raw, size = decksize, times = shuffles, target = 2020)
print("Solution:", part2)