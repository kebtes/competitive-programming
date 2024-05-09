# Problem: A - Problemsolving Log - https://codeforces.com/gym/522997/problem/A

for _ in range(int(input())):
    n = int(input())
    s = input()

    cnt = [0] * 26

    for i in range(n):
        cnt[ord(s[i]) - ord('A')] += 1
    output = 0

    for i in range(26):
        if cnt[i] >= i + 1:
            output += 1

    print(output)

