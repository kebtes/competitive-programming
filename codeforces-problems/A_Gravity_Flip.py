columns = int(input())
cubes = list(map(int, input().split()))

length = len(cubes) - 1

for i in range(length,0,-1):
    sub = cubes[:i]
    high = max(cubes[:i+1])
    index = cubes.index(high)

    difference = high-cubes[i]

    cubes[i] += difference
    cubes[index] -= difference

print(" ".join(map(str, cubes)))