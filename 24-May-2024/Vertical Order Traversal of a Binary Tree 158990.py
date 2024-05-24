# Problem: Vertical Order Traversal of a Binary Tree - https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        node_list = []

        def func(node, x, y):
            if node:
                node_list.append((x, y, node.val))
                func(node.left, x - 1, y + 1)
                func(node.right, x + 1, y + 1)

        func(root, 0, 0)

        node_list.sort(key=lambda x: (x[0], x[1], x[2]))

        vertical_dict = defaultdict(list)
        for x, y, value in node_list:
            vertical_dict[x].append(value)

        result = [vertical_dict[key] for key in sorted(vertical_dict.keys())]

        return result
