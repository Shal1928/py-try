import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    row = input()
    print(re.sub('[0]', '-', row))
