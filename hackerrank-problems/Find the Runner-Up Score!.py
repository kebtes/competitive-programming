if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
        
    max_num = float('-inf')
    runner_up = float('-inf')
    
    for num in arr:
        if num > max_num:
            runner_up = max_num
            max_num = num
        elif num > runner_up:
            runner_up = num
    
    print(runner_up)