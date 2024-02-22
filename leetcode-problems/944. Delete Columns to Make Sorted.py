class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        row = len(strs)
        col = len(strs[0])

        count = 0

        for c in range(col):
            colx = []
            for r in range(row):
                colx.append(strs[r][c])

            x = sorted(colx)
            if colx != x:
                count += 1
        
        return count


        