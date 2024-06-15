# Problem:  King Escape - https://codeforces.com/problemset/problem/1033/A

# import sys

# sys.setrecursionlimit(99999)

# n = int(input())

# alice_queen = list(map(int, input().split()))
# bob_king = list(map(int, input().split()))
# destination = list(map(int, input().split()))

# diagonals = [alice_queen[0] - alice_queen[1], alice_queen[0] + alice_queen[1]]
# visited_cells = set()

# def backtrack(row, col):
#     if [row, col] == destination:
#         return True
    
#     if row >= n or row < 0 or col >= n or col < 0 or (row, col) in visited_cells:
#         return False
    
#     if row-col in diagonals or row+col in diagonals or row == alice_queen[0] or col == alice_queen[1]:
#         return False
    
#     visited_cells.add((row, col))
    
#     return (backtrack(row + 1, col) or
#             backtrack(row - 1, col) or
#             backtrack(row, col + 1) or
#             backtrack(row, col - 1) or
#             backtrack(row + 1, col + 1) or
#             backtrack(row - 1, col - 1) or
#             backtrack(row + 1, col - 1) or
#             backtrack(row - 1, col + 1))

# if backtrack(bob_king[0], bob_king[1]): print("YES")
# else: print("NO")

n = int(input())

alice_queen = list(map(int, input().split()))
bob_king = list(map(int, input().split()))
destination = list(map(int, input().split()))

def func():
    if (bob_king[0] < alice_queen[0]) == (destination[0] < alice_queen[0]) and (bob_king[1] < alice_queen[1]) == (destination[1] < alice_queen[1]):
        return "YES"
    else:
        return "NO"

print(func())