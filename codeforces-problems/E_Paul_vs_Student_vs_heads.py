n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

for i in range(1, n):
    arr1[i] += arr1[i-1]

for i in range(1, m):
    arr2[i] += arr2[i-1]

idx = 0
jdx = 0
cnt = 0

if arr1[-1] != arr2[-1]:
    print("-1")
    exit()

while idx < len(arr1) and jdx < len(arr2):
    if arr1[idx] > arr2[jdx]:
        jdx += 1
    elif arr1[idx] < arr2[jdx]:
        idx += 1
    else:
        idx += 1
        jdx += 1
        cnt += 1


print(cnt)