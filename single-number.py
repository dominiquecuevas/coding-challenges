def single_number(nums):
    
    nums.sort()
    i = 0
    while i < len(nums):
        if i+3 < len(nums) and nums[i] == nums[i+1]:
            i += 2
        elif i+2 < len(nums) and nums[i+1] == nums[i+2]:
            return nums[i]
        else:
            i += 2
            return nums[i]

print(single_number([2,2,1]))
print(single_number([4,1,2,1,2]))