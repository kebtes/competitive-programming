# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

n = int(input())

def func(num):
    d = 2
    primes = set()

    while num > 1:
        while num % d == 0:
            num //= d
            primes.add(d)
        d += 1
    
        if d * d > num and num > 1:
            primes.add(num)
            break

    return len(primes) == 2

cnt = 0
for num in range(2, n+1):  
    if func(num):
        cnt += 1

print(cnt)
