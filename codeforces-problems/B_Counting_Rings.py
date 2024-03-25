text = list(input().lower())
output = 0
l = len(text)

cnt = 0
for i in range(l):
    if text[i] == "o":
        cnt += 1
    else:
        output = max(output, cnt)
        cnt = 0

output = max(output, cnt)

print(output)