import math

N = int(input())
nums = map(int, input().split())

negative_set = []
positive_set = []
zero_set = []

for num in nums:
    if num < 0:
        negative_set.append(num)
    elif num > 0:
        positive_set.append(num)
    else:
        zero_set.append(num) 

while not positive_set or math.prod(positive_set) < 0:
    positive_set.append(negative_set.pop())

while math.prod(negative_set) > 0:
    zero_set.append(negative_set.pop())

print(len(negative_set), *negative_set)
print(len(positive_set), *positive_set)
print(len(zero_set), *zero_set)