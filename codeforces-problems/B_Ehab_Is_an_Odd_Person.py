n = int(input())
nums = list(map(int, input().split()))
 
odd = [num for num in nums if num % 2 != 0]
even = [num for num in nums if num % 2 == 0]
 
if len(odd) and len(even):
    print(*sorted(nums))
else:
    print(*nums)