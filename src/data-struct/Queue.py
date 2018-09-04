class QueueTry:
    def __init__(self):
        self.list = []

    def enqueue(self, value):
        self.list.append(value)

    def dequeue(self):
        if self.list:
            self.list.pop(0)

    def __repr__(self):
        return ', '.join(str(i) for i in self.list)


class QueueTry2:
    def __init__(self):
        self.list = []

    def enqueue(self, value):
        self.list.insert(0, value)

    def dequeue(self):
        if self.list:
            self.list.pop()

    def __repr__(self):
        return ', '.join(str(i) for i in self.list)


queue = QueueTry2()
print('Queue = {0}'.format(queue))
queue.enqueue(1)
print('Queue = {0}'.format(queue))
queue.enqueue(2)
print('Queue = {0}'.format(queue))
queue.enqueue(3)
print('Queue = {0}'.format(queue))
queue.dequeue()
print('Queue = {0}'.format(queue))
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
print('Queue = {0}'.format(queue))
