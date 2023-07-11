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
    
customQueue = Queue()
customQueue.enqueue(1)
print(customQueue)