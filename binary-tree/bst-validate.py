# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], minRoot=None, maxRoot=None) -> bool:
        if root is None:
            return True
        if minRoot is None:
            minRoot = -sys.maxsize
            maxRoot = sys.maxsize
        if root.left and (root.left.val >= maxRoot or root.left.val <= minRoot or root.left.val >= root.val):
            return False
        if root.right and (root.right.val >= maxRoot or root.right.val <= minRoot or root.right.val <= root.val):
            return False
        return self.isValidBST(root.left, minRoot, root.val) and self.isValidBST(root.right, root.val, maxRoot)
            