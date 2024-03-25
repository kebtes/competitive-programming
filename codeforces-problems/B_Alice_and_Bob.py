N = int(input())

for _ in range(N):
    n, m, k = map(int, input().split())

    arr1 = sorted(input())
    arr2 = sorted(input())

    i = 0
    j = 0

    output = []

    c_a = 0
    c_b = 0

    while i < n and j < m:
        if c_a < k and c_b == k:
            c_b = 0
            c_a += 1
            output.append(arr1[i])
            i += 1
        elif c_a == k and c_b < k:
            c_a = 0
            c_b += 1
            output.append(arr2[j])
            j += 1

        if i < n and j < m and c_a < k and c_b < k:
            if arr1[i] <= arr2[j]:
                c_a += 1
                c_b = 0
                output.append(arr1[i])
                i += 1
            else:
                c_b += 1
                c_a = 0
                output.append(arr2[j])
                j += 1

    print("".join(output))
