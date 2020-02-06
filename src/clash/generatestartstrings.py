c = input()
l = int(input())
g = l % 2
if g == 0:
    print("CAN'T")
else:
    s = '*' * (l // 2)
    print(s + c + s)
