class priorityqueue:
    def __init__(self):
        self.queue = []
        
    def insert(self,item):
        self.queue.append(item)
        self.queue = self.mergesort(self.queue)
        
    def remove(self):
        if len(self.queue) == 0:
            print ("Kosong")
            return None
        return self.queue.pop(0)
    
    def mergesort(self, arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        return self.merge(left_half, right_half)
    
    def merge(self, left, right):
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i]< right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def print(self):
        print("Priority queue = ", self.queue)

pq= priorityqueue()
pq.insert(10)
pq.insert(1)
pq.insert(5)
pq.insert(3)

pq.print()
print("Removed =", pq.remove)
pq.print()