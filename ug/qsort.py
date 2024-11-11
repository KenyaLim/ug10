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
        return self.queue[0][0], self.queue[0][1]
    
    #PRIORITAS TERBESAR KE TERKECIL!
    def add(self, name, priority):
        if self.is_empty():
            self.queue.append((name, priority))
        else:
            for i in range(len(self.queue)):
                if priority >= self.queue[i][1]:
                    self.queue.insert(i, (name, priority))
                    break
        
    def print_all(self):
        print(self.queue)
    def partition(data, start, end):
        pivot = data[end]
        left = start
        right = end - 1
        
        while True:
            while left <= right and data[left] < pivot:
                left += 1
            while left <= right and data[right] > pivot:
                right -= 1
            
            if left <= right:
                # Swap
                data[left], data[right] = data[right], data[left]
                left += 1
                right -= 1
            else:
                break
            
    def quicksort(data, start, end):
        if start < end:
            pivot = partition(data, start, end)
            quicksort(data, start, pivot - 1)
            quicksort(data, pivot + 1, end)
            
    def add(self,data, priority):
        self.queue.append(priority,data)
        quicksort(self.queue, 0 (len(self.queue) - 1)
                