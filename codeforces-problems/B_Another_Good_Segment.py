n, s = map(int, input().split())
lst = list(map(int, input().split()))

seen = {}
cnt = 0
l = 0

for r in range(n):
    seen[lst[r]] = seen.get(lst[r], 0) + 1

    while len(seen) > s:
        seen[lst[l]] -= 1
        if seen[lst[l]] == 0:
            del seen[lst[l]]
        l += 1
    cnt += r-l+1

print(cnt)