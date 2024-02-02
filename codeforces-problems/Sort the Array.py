def is_sortable_array(n, nums):
    if nums == sorted(nums):
        return True, 1, 1

    start = -1
    end = -1
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            start = i
            break
    for i in range(n - 1, 0, -1):
        if nums[i] < nums[i - 1]:
            end = i
            break

    reversed_nums = nums[:start] + nums[start:end+1][::-1] + nums[end+1:]
    if reversed_nums == sorted(nums):
        return True, start + 1, end + 1

    reversed_nums = nums[:start] + nums[start:end][::-1] + nums[end:]
    if reversed_nums == sorted(nums):
        return True, start + 1, end

    return False, 0, 0


n = int(input())
nums = list(map(int, input().split()))

sortable, start, end = is_sortable_array(n, nums)

if sortable:
    print("yes")
    print(start, end)
else:
    print("no")