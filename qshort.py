def partition(data, start, end):
    pivot = data[end]
    left = start
    right = end - 1
    
    while True:
        while left <= right and data[left] > pivot:
            left += 1
        while left <= right and data[right] < pivot:
            right -= 1
        
        if left <= right:
            # Swap
            data[left], data[right] = data[right], data[left]
            left += 1
            right -= 1
        else:
            break
    
    # Swap the pivot element with the left index
    data[left], data[end] = data[end], data[left]
    return left  # Return the index of the pivot

def quicksort(data, start, end):
    if start < end:
        pivot = partition(data, start, end)
        quicksort(data, start, pivot - 1)
        quicksort(data, pivot + 1, end)

listx = [10, 1, 0, 20, 12, 2, 30, 30, 60, 15]
print(listx)
quicksort(listx, 0, len(listx) - 1)
print(listx)