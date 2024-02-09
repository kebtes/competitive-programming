stops = int(input())
max_sits = 0

capacity = 0

for _ in range(stops):
    exits, enters = list(map(int, input().split()))

    capacity -= exits
    capacity += enters

    max_sits = max(max_sits, capacity)

print(max_sits)




