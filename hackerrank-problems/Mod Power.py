# Enter your code here. Read input from STDIN. Print output to STDOUT

def power(a,b,m = None):
    print(a**b, end = "\n")
    if m: print((a**b)%m)
    
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    m = int(input())
    
    power(a,b,m)