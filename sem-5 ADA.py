def bubblesort (nums):
 
    for i in range(0,len(nums)):
        for j in range (len(nums)-i-1):
            if (nums[j]>nums[j+1]):
                swap=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=swap


n=int(input("enter size of array:"))
nums=[]
for i in range (n):
    val=int(input("enter value:"))
    nums.append(val)
    
bubblesort(nums)
print(nums)



