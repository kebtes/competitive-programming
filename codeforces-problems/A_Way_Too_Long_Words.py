N = int(input())

for _ in range(N):
    word = input()
    length = len(word)

    if length > 10:
        print(f"{word[0]}{length-2}{word[-1]}")
    else:
        print(word)