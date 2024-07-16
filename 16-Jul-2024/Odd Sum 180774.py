# Problem: Odd Sum - https://codeforces.com/problemset/problem/797/B

n = int(input())
nums = list(map(int, input().split()))

odd_sequence = float('-inf')
even_sequence = 0

for num in nums:
    if num % 2 == 0:
        new_odd_sequence = max(odd_sequence, odd_sequence + num)
        new_even_sequence = max(even_sequence, even_sequence + num)
    else:
        new_odd_sequence = max(odd_sequence, even_sequence + num)
        new_even_sequence = max(even_sequence, odd_sequence + num)
    
    odd_sequence = new_odd_sequence
    even_sequence = new_even_sequence

print(odd_sequence)
