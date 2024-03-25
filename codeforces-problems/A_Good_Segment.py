n = int(input())
txt = input().lower()

long_seg = 1
cur_seg = 1

for idx in range(1, n):
    if ord(txt[idx]) - ord(txt[idx-1]) == 1:
        cur_seg += 1
    else:
        cur_seg = 1

    long_seg = max(long_seg, cur_seg)

print(long_seg)

#abcdzdfghj