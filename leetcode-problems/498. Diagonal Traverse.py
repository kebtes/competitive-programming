class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        r = len(mat)
        c = len(mat[0])
    
        output = []
        matrix_dict = {}
    
        for r_idx in range(r):
            for c_idx in range(c):
                if r_idx + c_idx not in matrix_dict:
                    matrix_dict[r_idx + c_idx] = [mat[r_idx][c_idx]]
                else:
                    matrix_dict[r_idx + c_idx].append((mat[r_idx][c_idx]))
        
        for m in matrix_dict.items():
            if m[0] % 2 == 0:
                [output.append(x) for x in m[1][::-1]]
            else:
                [output.append(x) for x in m[1]]
    
        return output