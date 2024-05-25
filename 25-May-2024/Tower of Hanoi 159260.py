# Problem: Tower of Hanoi - https://www.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1

# User function Template for python3

class Solution:
    def toh(self, N, fromm, to, aux):
        if (N == 1):
            print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
            return 1
        
        mvs = 0
        mvs += self.toh(N-1, fromm, aux, to) + 1
        
        print("move disk", str(N), "from rod", str(fromm), "to rod", str(to))
        mvs += self.toh(N-1, aux, to, fromm)
        return mvs


#{ 
 # Driver Code Starts
# Initial Template for Python 3


import math


def main():

    T = int(input())

    while(T > 0):
        N = int(input())
        ob = Solution()
        print(ob.toh(N, 1, 3, 2))
        T -= 1
if __name__ == "__main__":
    main()


# } Driver Code Ends