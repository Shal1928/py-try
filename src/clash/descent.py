import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
m = []
while True:
    for i in range(8):
        m.append(int(input()))
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # The index of the mountain to fire on.
    print(m.index(max(m)))
    m = []

# best solution:
# while True:
#     print(max([(int(input()),x) for x in range(8)])[1])

# while True:
#     m = [int(input()) for i in range(8)]  # represents the height of one mountain.
#
#     # Write an action using print
#     # To debug: print("Debug messages...", file=sys.stderr)
#
#     # The index of the mountain to fire on.
#     print(m.index(max(m)))
