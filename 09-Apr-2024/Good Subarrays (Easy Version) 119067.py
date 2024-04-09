# Problem: Good Subarrays (Easy Version) - https://codeforces.com/problemset/problem/1736/C1

N = int(input())

for _ in range(N):
    n = int(input())
    arr = list(map(int,input().split()))
    
    l=0
    j=1

    cnt=0
    
    for r in range(n):
        while l < n and j > arr[r]:
            l += 1
            j -= 1

        cnt += r - l + 1
        j+=1

    print(cnt)
