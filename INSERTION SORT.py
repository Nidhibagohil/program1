

def sort(num):
    for i in range(len(num)):
        key = num[i]
        j = i - 1
        while j >= 0 and num[j] > key:
            num[j + 1] = num[j]
            j -= 1
        num[j + 1] = key

# Input list
num = [4, 3, 2, 2, 1]

# Sorting the list
sort(num)

# Print the sorted list
print(num)
