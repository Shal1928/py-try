class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return "{0}:n{1}".format(str(self.data), str(self.next))

class LinkedList:
    def __init__(self):
        self.list = []
        self.index = 0;

    # def add(self, value, index):
    #     self.list.append(Node(value, index))

    def add(self, value):
        self.index += 1
        self.add(value, self.index)

    def remove(self):
        self.list.pop()

    def __repr__(self):
        return ', '.join(str(i) for i in self.list)