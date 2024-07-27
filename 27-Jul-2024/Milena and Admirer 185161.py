# Problem: Milena and Admirer - https://codeforces.com/problemset/problem/1898/B

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    
    op = 0

    for i in range(n - 2, -1, -1):
        if nums[i] > nums[i+1]:
            parts = (nums[i] + nums[i+1] - 1) // nums[i+1]
            new_value = nums[i] // parts
            op += parts - 1
            nums[i] = new_value

    print(op)

