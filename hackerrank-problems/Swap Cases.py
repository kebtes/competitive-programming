def swap_case(s):
    output = ""
    
    for char in s:
        if char.islower():
            output += str(char.upper())
        elif char.isupper():
            output += str(char.lower())
        else:
            output += str(char)
            
    return output

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)