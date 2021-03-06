class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return "{0}:n{1}".format(str(self.data), str(self.next))


class LinkedList:
    def __init__(self):
        self.list = []
        self.index = 0

    def add(self, value):
        self.index += 1
        self.list.append(Node(value, self.index))

    def insert(self, value, index):
        self.add(None)
        for node in self.list[::-1]:
            if self.index == node.next:
                continue
            i = self.list.index(node)
            node.next += 1
            self.list[i + 1] = node
            if i == index:
                self.list[i] = Node(value, i+1)
                break

    def remove(self, index):
        if index <= self.index:
            self.list.pop(index)
        else:
            raise IndexError("Index {0} is out of range!".format(index))

    def __repr__(self):
        return ", ".join(str(i) for i in self.list)


linkedList = LinkedList()
print("1 stack = {0}".format(linkedList))
linkedList.add(1)
linkedList.add(2)
print("2 stack = {0}".format(linkedList))
linkedList.insert(1.5, 1)
print("3 stack = {0}".format(linkedList))
linkedList.insert(1.4, 1)
print("3 stack = {0}".format(linkedList))
