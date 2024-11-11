def mergesort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]
        
        mergesort(left)
        mergesort(right)
        
        i = 0 
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] == right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1
listx=[10,1,0,20,12,2,30,30,60,15]
print(listx)
mergesort(listx)
print (listx)