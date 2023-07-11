class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    
    def enqueue(self,values):
        self.items.append(values)
        return "Yes the item is inserted"
    
    def dequeue(self):
        if self.isEmpty():
            return 'Queue is empty'
        else:
            return self.items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return 'Queue is empty'
        else:
            return f'{self.items[0]}'
    
    def delete(self):
        self.items = None
    
customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
# print(customQueue.dequeue())
print(customQueue.peek())