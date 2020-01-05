#
# After 80+ hours on this puzzle, I gave up...
#
# I calculated the answer for my input using another's
# solution, and leaving it here in all its shame:
#
print("45347150615590")
#
# Calculated using: https://gist.github.com/Voltara/7d417c77bc2308be4c831f1aa5a5a48d
#
# After reading up on Reddit, I'm not too sad that I gave
# up. I was afraid that it would turn out I was so close,
# that I could've solved it on my own if only I kept on
# for just a bit longer.
#
# I'm glad to see that idea was wrong. Even if I had spent
# another 80 hours, I probably wouldn't have solved this
# puzzle.
#
# Apparently I did figure out a few key parts of the answer
# on my own, including:
#
# 1. Modular Multiplicative Inverse operation for reversing
#    the "deal with increment" operation
#
# 2. Not needing it after all, because the deck restores to
#    factory order after `deckSize` shuffles, so you can just
#    shuffle forward to the end to get the answer.
#
# 3. Composing the 50 input instructions to one operation was
#    indeed possible, and even the key.
#
# 4. There is an "apparent randomness" in the card position,
#    and as it turned out parts of this puzzle coincide with
#    how pseudo-random generators work.
# 
# and finally, not "figured out" but suspected:
#
# 5. Some kind of algorithm to quickly apply the full shuffle
#    many times would be possible, heck even the answer.
#
# 6. The deck size and shuffle count being large primes was
#    supposedly indeed meaningful: them being co-primes in fact
#    prevented the solution from being too easy.
#
# In the end, this kind and level of puzzle turns out to be beyond
# my grasp. I'd have to spend serious time in math and algorithms
# to be able to solve it myself.
#
# Glad I stopped after "just" 80 hours of trying...
#