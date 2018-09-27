objects = [1, 2, 3, 3, 3, 'Hello', {'4'}, 0, True]
s = set(id(x) for x in objects)
print(s.__len__())
