def pokemon(nums):
    return min(len(nums)//2, len(set(nums)))





print(pokemon([3,1,2,3])) # result = 2
print(pokemon([3,3,3,2,2,4])) # result = 3
print(pokemon([3,3,3,2,2,2])) # result = 2