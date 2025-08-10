def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less  = [x for x in arr[1:] if x <= pivot]
    more  = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(more)


arr = [5, 2, 9, 1, 5, 6]
print("Sorted:", quick_sort(arr))
