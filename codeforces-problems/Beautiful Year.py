y = int(input())

while True:
    y += 1

    a = int(y/1000)
    b = int(y / 100 % 10)
    c = int(y / 10 % 10)
    d = int(y % 10)
     
    if a != b and a != c and a != d and b != c and b != d and c != d:
        break

print(y)