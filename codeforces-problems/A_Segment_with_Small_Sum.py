n, s = map(int, input().split())
nums = list(map(int, input().split()))

max_len = 0
window_sum = 0
left = 0

for right in range(n):
    window_sum += nums[right]

    while window_sum > s:
        window_sum -= nums[left]
        left += 1

    max_len = max(max_len, right - left + 1)

print(max_len)