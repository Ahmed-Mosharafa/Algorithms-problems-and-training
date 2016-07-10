class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        if len(self.storage) > 0:
            self.storage = [new_element] + self.storage
        else:
            self.storage.append(new_element)

    def peek(self):
        if len(self.storage)>0:
            return self.storage[-1]
        else:
            return None

    def dequeue(self):
        if len(self.storage) >0:
            return self.storage.pop()
        else:
            return None