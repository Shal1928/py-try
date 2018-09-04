class StackTry:
    def __init__(self):
        self.list = []

    def push(self, new_element):
        self.list.append(new_element)

    def pop(self):
        if self.list:
            self.list.pop()

    def __repr__(self):
        return ', '.join(str(i) for i in self.list)


stack = StackTry()
print('1 stack = {0}'.format(stack))
stack.push(1)
stack.push(2)
print('2 stack = {0}'.format(stack))
stack.pop()
print('3 stack = {0}'.format(stack))
stack.pop()
stack.pop()
stack.pop()
print('4 stack = {0}'.format(stack))
