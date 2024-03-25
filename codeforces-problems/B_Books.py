n, minutes = map(int, input().split())
books = list(map(int, input().split()))

cum_sum = 0
cnt = 0
k = 0

for idx in range(n):
    cum_sum += books[idx]

    if cum_sum <= minutes:
        cnt += 1
    else:
        cum_sum -= books[k]
        k += 1

print(cnt)
