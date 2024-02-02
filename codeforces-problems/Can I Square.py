def can_be_square(n):
    from math import sqrt
    
    sqrt_n = int(sqrt(n))

    if sqrt_n**2 == n:
        return "YES"
    return "NO"

t = int(input())
results = []

for i in range(t):
    buckets = int(input())
    squares = list(map(int, input().split()))
    sums = sum(squares)

    results.append(can_be_square(sums))

print("\n".join(results))