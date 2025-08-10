

def bubblesort (nums):
 
    for i in range(0,len(nums)):
        for j in range (len(nums)-i-1):
            if (nums[j]>nums[j+1]):
                swap=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=swap

nums=[4,3,1,5,2]
bubblesort(nums)
print("sorted",nums)







                    
