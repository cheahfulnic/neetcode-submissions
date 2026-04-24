# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def depth(node):
            if node is None:
                return 0
            left = depth(node.left)
            right = depth(node.right)

            height_diff = abs(left - right)

            if height_diff > 1:
                self.balanced = False

            return 1 + max(left, right)

        depth(root)
        return self.balanced