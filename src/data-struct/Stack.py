class StackTry:
    def __init__(self):
        self.list = []

    def push(self, newElement):
        self.list.append(newElement)

    def pop(self):
        self.list.pop()
