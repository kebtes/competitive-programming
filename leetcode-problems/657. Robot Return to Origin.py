class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        i=j=0
    
        for m in moves:
            if m == "L": j -= 1
            elif m == "R": j += 1
            elif m == "U": i -= 1
            else: i +=1
        
        return i == 0 and j == 0
        """
        return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")