# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            elif p.val != q.val:
                return False

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        if subRoot is None:
            return True
        if root is None:
            return False

        stack = [root]
        while stack:
            node = stack.pop()
            if isSameTree(node, subRoot):
                return True

            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)

        return False

