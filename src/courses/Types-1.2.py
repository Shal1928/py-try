objects = [1, 2, 3, 3, 3, 'Hello', {'4'}, 0, True]
s = set()
for obj in objects:
    s.add(id(obj))
print(s.__len__())


