n = int(input())
fingers = list(map(int, input().split()))
 
total = sum(fingers)
ways = 0
 
for i in range(1, 6):
    if (total + i) % (n + 1) != 1:
        ways += 1
 
print(ways)