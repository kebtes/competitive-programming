N = int(input())
nums = list(map(int, input().split()))


if sum(nums[:N]) != sum(nums[N:]):
    print(*nums)
    exit()
    
nums.sort()

if len(nums) % 2 != 0:
    print('-1')
    exit()

arr1 = nums[:N]
arr2 = nums[N:]

if sum(arr1) != sum(arr2):
    print(*nums)
else:
    print("-1")