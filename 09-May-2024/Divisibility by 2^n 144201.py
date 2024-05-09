# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

def func(num):
    cnt = 0

    while num % 2 == 0:
        num //= 2
        cnt += 1

    return cnt

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    total = 0
    indices = [0] * n

    for num in nums:
        total += func(num)

    if total >= n:
        print(0)
        continue
    
    for i in range(1, n + 1):
        indices[i - 1] += func(i)
    
    indices.sort(reverse=True)
    op = 0

    for i in range(n):
        total += indices[i]
        op += 1
        if total >= n:
            print(op)
            break
    
    if total < n:
        print(-1)