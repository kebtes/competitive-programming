N = int(input())
phone_book = {}
output = []

for _ in range(N):
    inp = input()
    name, phone = inp.split()

    phone_book[name] = phone

for _ in range(N):
    output.append(str(input))

for name in output:
    if name in phone_book:
        print(f"{name}={phone_book[name]}")
    else:
        print("Not Found")
