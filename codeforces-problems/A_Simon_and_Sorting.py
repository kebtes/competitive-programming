
if "__name__" == "__main__":
    N = int(input())
    WORD = "abc"    

    for _ in range(N):
        text = str(input()).lower()
        c = 0

        if text == WORD:
            print("YES")
            continue
        else:
            for i in range(3):
                if text[i] != WORD[i]:
                    c += 1

        if c == 2: print("YES")
        else: print("NO")