

def sort(num):
    for i in range(len(num)):
        key = i
        for j in range(i + 1, len(num)):
            if num[j] < num[key]:
                key = j
        num[i], num[key] = num[key], num[i]

# Input list
num = [70, 46, 76, 45, 98, 23]

# Sorting the list
sort(num)

# Print the sorted list
print(num)
