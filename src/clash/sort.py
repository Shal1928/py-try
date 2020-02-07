n = int(input())
s = []
for i in input().split():
    s.append(int(i))
s.sort()
r = ''
space = ''
f = True
for i in s:
    if f:
        r = r + space + str(i)
        f = False
    else:
        space = ' '
        r = r + space + str(i)
print(r)