# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getNodes(self, root, l=None):
        if l is None:
            l = []
        if root is None:
            return l
        self.getNodes(root.left, l)
        l.append(root.val)
        self.getNodes(root.right, l)
        return l

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        l = self.getNodes(root)
        diff = l[1] - l[0]
        n = len(l)-1
        for i in range(n):
            diff = min(diff, l[i+1]-l[i])
        return diff