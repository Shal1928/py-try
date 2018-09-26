objects = [1, 2, 3, 3, 3, 'Hello', {'4'}, 0]
s = set()
for obj in objects:
    s.add(objects.index(obj))
print(s.__len__())


