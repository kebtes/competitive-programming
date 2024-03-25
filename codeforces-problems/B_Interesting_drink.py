import bisect

n = int(input())
prices = list(map(int, input().split()))
days = int(input())

last_idx = 0
prices.sort()


for _ in range(days):
    coin = int(input())
    position = bisect.bisect(prices, coin)
    print(position)