# Problem: Team Composition: Programmers and Mathematicians - https://codeforces.com/problemset/problem/1611/B

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(min(min(a,b), (a+b) // 4))