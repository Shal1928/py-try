objects = [1, 2, 3, 3, 3, 'Hello', {'4'}, 0, True]
print(len(set(map(id, objects))))
