def func(arr1, arr2, n):
    sorted_arr1 = sorted(arr1)
    sorted_arr2 = sorted(arr2)

    output = []
    is_solved = True

    for i in range(n):
        if arr1[i] != sorted_arr1[i] or arr2[i] != sorted_arr2[i]:
            for j in range(i+1, n):
                if arr1[j] == sorted_arr1[i] and arr2[j] == sorted_arr2[i]:
                    output.append([j+1, i+1])
                    arr1[i], arr1[j] = arr1[j], arr1[i]
                    arr2[i], arr2[j] = arr2[j], arr2[i]     
                    break   
            else:
                print("-1")
                is_solved = False
                break

    if is_solved:
        print(len(output))
        for x in output:
            print(*x)


if __name__ == "__main__":
    P = int(input())
    for _ in range(P):
        n = int(input())
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
        
        func(arr1, arr2, n)