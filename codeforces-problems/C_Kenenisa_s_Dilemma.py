N = int(input())
nums = list(map(int, input().split()))

sorted_nums = sorted(nums)
output = []

for i in range(N):
    if nums[i] != sorted_nums[i]:
        for j in range(i+1, N):
            if nums[j] == sorted_nums[i]:
                output.append((i, j))
                nums[i], nums[j] = nums[j], nums[i]
                break

print(len(output))
for n in output:
    print(*n, end = "\n")