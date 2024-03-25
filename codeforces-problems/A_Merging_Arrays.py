n, m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

i = j = 0

output = []

while i < n and j < m:
    if arr1[i] >= arr2[j]:
        output.append(arr2[j])
        j += 1
    else:
        output.append(arr1[i])
        i += 1

while arr1[i:]:
    output.append(arr1[i])
    i += 1

while arr2[j:]:
    output.append(arr2[j])
    j += 1
    
print(*output)