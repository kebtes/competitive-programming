N = int(input())

for _ in range(N):
    players = int(input()) 
    strength = list(map(int, input().split()))
    strength.sort()
    mini_strength = float('inf')

    for i in range(players -1):
        mini_strength = min(mini_strength, strength[i+1] - strength[i])

    print(mini_strength)