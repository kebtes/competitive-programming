# Problem: Validate Binary Tree Nodes - https://leetcode.com/problems/validate-binary-tree-nodes/

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parents = set(leftChild + rightChild)
        parents.discard(-1)

        if len(parents) == n:
            return False

        root = -1
        for idx in range(n):
            if idx not in parents:
                if root == -1:
                    root = idx
                else:
                    return False

        if root == -1:
            return False

        visited = set()
        def func(node):
            if node == -1:
                return True
            
            if node in visited:
                return False

            visited.add(node)
            return func(leftChild[node]) and func(rightChild[node])

        return func(root) and (len(visited) == n)
        