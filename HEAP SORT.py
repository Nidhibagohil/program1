def heapify(arr,n,i):
    while True:
        largest=i
        left=2*i+1
        right=2*i+2
        if left < n and arr[left] > arr[largest]:
            largest=left
        if right < n and arr[right] > arr[largest]:
            largest=right
        if largest==i:
              break
        arr[i], arr[largest]= arr[largest], arr[i]
        i=largest

def heap_sort(arr):
    n=len(arr)
    for i in reversed(range(n // 2)):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]

        heapify(arr,i,0)
arr=[3,4,5,1,2,8,]
print("original Array:",arr)
heap_sort(arr)
print("Sorted Array(ascending):",arr)
