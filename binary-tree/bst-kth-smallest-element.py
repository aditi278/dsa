# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int, l=None) -> int:
        if l is None:
            l = []
        if root is None:
            return -1
        val = self.kthSmallest(root.left, k, l)
        if val is not None and val != -1:
            return val
        l.append(root.val)
        if len(l) == k:
            return l[k-1]
        elif k < 0:
            return -1
        val = self.kthSmallest(root.right, k, l)
        if val is not None and val != -1:
            return val
