# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode], l=None, level=0) -> List[int]:
        if l is None:
            l = []
        if root is None:
            return l
        if len(l)<=level:
            l.append(root.val)
        self.rightSideView(root.right, l, level+1)
        self.rightSideView(root.left, l, level+1)
        return l