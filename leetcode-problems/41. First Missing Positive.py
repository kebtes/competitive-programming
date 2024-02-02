def firstMissingPositive(nums):  
    """
    time complexity -> O(n log n)
    auxillary space -> O(1)
    space complexity -> O(1)
    """

    smallest = 1

    nums.sort()

    for num in nums:
        if num == smallest:
            smallest += 1
        
    return smallest

print(firstMissingPositive([1,2,0]))
#print(firstMissingPositive([3,4,-1,1]))
#print(firstMissingPositive([0])) 