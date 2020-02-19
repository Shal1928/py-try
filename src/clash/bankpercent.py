n, i, m = [int(i) for i in input().split()]
for j in range (m):
    n+=n*(i/100)
print(int(n))