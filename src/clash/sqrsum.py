r = 0;
n = int(input())
for i in input().split():
    r = int(i) ** 2 + r
print(r)