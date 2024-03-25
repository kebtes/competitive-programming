N = int(input())

for _ in range(N):
    n = int(input())
    arr = list(map(int, input().split()))
    temp_arr = []

    for num in arr:
        if temp_arr and num > 0 and temp_arr[-1] > 0:
            temp_arr[-1] = max(num, temp_arr[-1])
        elif temp_arr and num < 0 and temp_arr[-1] < 0:
            temp_arr[-1] = max(num, temp_arr[-1])
        else:
            temp_arr.append(num)
    
    print(sum(temp_arr))

