n = int(input())
nums = list(map(int, input().split()))

nums.sort()

output = [nums[0]]

j = n-1
i = 1

for k in range(1, n):
    if k % 2 != 0:
        if nums[j] < output[k-1]:
            print("Impossible")
            exit()
        output.append(nums[j])
        j -= 1
    else:
        if nums[i] > output[k-1]:
            print("Impossible")
            exit()
        output.append(nums[i])
        i += 1
    
print(*output)