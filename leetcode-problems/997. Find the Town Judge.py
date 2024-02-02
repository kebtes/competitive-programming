class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        trust_me = [0] * (n+1)
        i_trust = [0] * (n+1)
        
        for a, b in trust:
            trust_me[b] += 1
            i_trust[a] += 1
    
        for i in range(1,n+1):
            if trust_me[i] == n - 1 and i_trust[i] == 0:
                return i
        
        return -1