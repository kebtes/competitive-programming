n = int(input())

dict = {}
files = []

for _ in range(n):
    file_name = input()

    if file_name in dict:
        count = dict[file_name] + 1
        new_name =f"{file_name}{count}"
        dict[file_name] = count
        print(new_name)
    else:
        print("OK")
        dict[file_name] = 0
