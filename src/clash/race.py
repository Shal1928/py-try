import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    s, t = [int(j) for j in input().split()]
    if s==0:
        print(0)
    else:
        print(int(t*60/(100/s)))