# Problem: Minimal string - https://codeforces.com/contest/797/problem/C

from collections import Counter

def func(s):
    def find_smallest_char(remaining):
        for i in range(26):
            char = chr(ord('a') + i)
            if remaining[char] > 0:
                return char
        return None

    result = []  # final result (u)  
    temp_stack = []  # intermediate stack (t)

    remaining_chars = Counter(s)

    for char in s:
        temp_stack.append(char)
        remaining_chars[char] -= 1

        while temp_stack:
            smallest_char = find_smallest_char(remaining_chars)
            if smallest_char is None or temp_stack[-1] <= smallest_char:
                result.append(temp_stack.pop())
            else:
                break

    while temp_stack:
        result.append(temp_stack.pop())

    return ''.join(result)


input_string = input()
result = func(input_string)
print(result)
