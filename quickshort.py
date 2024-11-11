def partition(data, start, end):
    pivot =data[end]
    left = start
    right = end-1
    while left <= right:
        while data[left]< pivot:
            left += 1
        while data[right]> pivot:
            left -= 1
        if left<= right:
            #swap
            data[left], data[right] = data[right], data[left]
            left +=1
            right -=1
    data[left], data[end] = data[end], data[left]
    return left

def quicksort(data, start, end):
    if start < end:
        pivot = partition(data,start,end)
        quicksort(data,start, pivot-1)
        quicksort(data, pivot+1, end)

listx=[10,1,0,20,12,2,30,30,60,15]
quicksort(listx,0,len(listx)-1)
print(listx)