number_of_events = int(input())
events = list(map(int, input().split()))

officers = 0
untreated = 0

for event in events:
    if event == -1:
        if not officers:
            untreated += 1
        else:
            officers -= 1
    else:
        officers += event

print(untreated)