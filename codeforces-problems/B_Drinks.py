N = int(input())
drink_sum = sum(list(map(int, input().split())))

ans = drink_sum / N
print("{:.12f}".format(ans))
