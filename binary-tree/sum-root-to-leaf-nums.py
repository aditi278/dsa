# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def getPaths(root, curr='', paths=None):
            if paths is None:
                paths = []
            curr+=str(root.val)
            if root.left is None and root.right is None:
                paths.append(curr)
            if root.left:
                paths = getPaths(root.left, curr, paths)
            if root.right:
                paths = getPaths(root.right, curr, paths)
            return paths
        paths = getPaths(root)
        totalSum = 0
        for x in paths:
            totalSum+=int(x)
        return totalSum
