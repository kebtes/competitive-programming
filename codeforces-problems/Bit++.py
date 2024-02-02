x = 0
n = int(input())

for i in range(n):
    statement = str(input()).replace("X", "")

    if statement == "--":
        x -= 1
    else:
        x += 1
    
print(x)