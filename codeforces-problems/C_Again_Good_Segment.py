n, k = map(int, input().split())
lst = list(map(int, input().split()))

count = 0
freq_dict = {}
l = 0

for r in range(n):
    freq_dict[lst[r]] = freq_dict.get(lst[r], 0) + 1

    while freq_dict and max(freq_dict.values()) >= k:
        freq_dict[lst[l]] -= 1
        if freq_dict[lst[l]] == 0:
            del freq_dict[lst[l]]
        l += 1

    count += l

print(count)