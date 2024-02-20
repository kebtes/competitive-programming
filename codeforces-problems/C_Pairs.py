from collections import Counter

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

a = Counter(a)
ans = 0

for i in c:
    ans+=a.get(b[i-1],0)

print(ans)