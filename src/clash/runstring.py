n = int(input())
text = input()
l = len(text)
for i in range(0,l):
    r=text[i:i+n]
    if len(r)==n:
        print(r)
