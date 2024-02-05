
if __name__ == '__main__':
    N = int(input())
    lst = []

    for _ in range(N):
        inp_text = list(input().split())
        command = inp_text[0]

        if command == "insert":
            lst.insert(int(inp_text[1]), int(inp_text[2]))
        elif command == "print":
            print(lst)
        elif command == "remove":
            lst.remove(int(inp_text[1]))
        elif command == "append":
            lst.append(int(inp_text[1]))
        elif command == "sort":
            lst.sort()
        elif command == "pop":
            lst.pop()
        elif command == "reverse":
            lst.reverse()