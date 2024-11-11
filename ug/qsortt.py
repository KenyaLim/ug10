class PriorityQueueSorted:
    def __init__(self):
        self.queue = []
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def len(self):
        return len(self.queue)
    
    def remove(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]
    
    # PRIORITAS TERBESAR KE TERKECIL!
    def add(self, name, priority):
        if self.is_empty():
            self.queue.append((name, priority))
        else:
            for i in range(len(self.queue)):
                if priority >= self.queue[i][1]:
                    self.queue.insert(i, (name, priority))
                    return 
            self.queue.append((name, priority))
        
    def print_all(self):
        print(self.queue)

### TEST CASE
myQueue = PriorityQueueSorted()
myQueue.add('Gian', 2)
myQueue.add('Kezia', 4)

myQueue.print_all()
#print("\nPEEK!\n")
myQueue.peek()
print()
myQueue.add('Glen', 8)
myQueue.add('Christo', 1)

myQueue.print_all()
#print("\nPEEK!\n")

myQueue.peek()
print()
#"""
print("========REMOVE========")
myQueue.remove()

myQueue.print_all()

print()
myQueue.remove()

myQueue.print_all()

print()
myQueue.remove()
myQueue.print_all()
print()
myQueue.add('Saya', 7)
myQueue.print_all()
#"""