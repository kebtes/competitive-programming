def remove_cons_pairs(text):
    stack = []

    for char in text:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    return "".join(stack)

text = input().strip()

print(remove_cons_pairs(text))