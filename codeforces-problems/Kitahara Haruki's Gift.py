# wrong solution

n = int(input())
apples = list(map(int, input().split()))

count_100 = apples.count(100)
count_200 = apples.count(200)

if count_100 % 2 == 0:
    if count_200 % 2 == 0 or count_100 > 0:
        print("YES") 
elif count_200 % 2 == 1 and count_100 > 0:
    print("YES") 
else: print("NO") 