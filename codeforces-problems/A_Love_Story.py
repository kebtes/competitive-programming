N = int(input())

word = "codeforces"

for _ in range(N):
    text = str(input()).lower()
    output = 0

    for i in range(len(text)):
        if text[i] != word[i]:
            output += 1

    print(output)