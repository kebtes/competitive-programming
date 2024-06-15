# Problem: New Year Transportation - https://codeforces.com/problemset/problem/500/A

from itertools import accumulate

n, t = map(int, input().split())
doors = list(map(int, input().split()))

cur_door = 1

for i in range(n):
    if (cur_door) == t:
        print("YES")
        exit()
    if (cur_door) > t:
        print("NO")
        exit()

    if cur_door == (i + 1):
        cur_door += doors[i]


     