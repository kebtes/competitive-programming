from collections import Counter

N = int(input())
boxes = sorted(list(map(int, input().split())))

count = Counter(boxes)
visible = max(count.values())

print(visible)