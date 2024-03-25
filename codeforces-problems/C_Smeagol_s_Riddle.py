N = int(input())

for _ in range(N):
    text = list(input().lower())
    n = len(text)

    cnt = 0

    i = 0
    j = n - 1

    while i < j:
        if text[i] != text[j]:
            cnt += 1
        
        i += 1
        j -= 1
    
    print(cnt)
