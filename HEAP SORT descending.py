def heapify(arr, n, i):
    while True:
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right
        if smallest == i:
            break
        arr[i], arr[smallest] = arr[smallest], arr[i]
        i = smallest

def heap_sort_descending(arr):
    n = len(arr)

    
    for i in reversed(range(n // 2)):
        heapify(arr, n, i)

    
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  
        heapify(arr, i, 0)


arr = [3, 4, 5, 1, 2, 8]
print("Original Array:", arr)
heap_sort_descending(arr)
print("Sorted Array (descending):", arr)
