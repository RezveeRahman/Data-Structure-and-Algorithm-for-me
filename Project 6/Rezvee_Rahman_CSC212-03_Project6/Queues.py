#Rezvee Rahman
#CSC212-03
#Queues

class Queue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return "Queue: {}".format(self.queue)
    
    def _enqueue(self, element):
        return self.queue.append(element)

    def _unqueue(self):
        return self.queue.pop(0)

    def _isEmpty(self):
        return len(self.queue) == 0

    def _size(self):
        return len(self.queue)

    def _peek(self, elempos):
        return self.queue[elempos]

