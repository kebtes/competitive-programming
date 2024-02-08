class Solution:
    def doUnion(self,a,n,b,m):
        return len(list(set(a) | set(b)))