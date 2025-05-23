# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        tmp = root.right
        if root.left:
            self.flatten(root.left)
            self.flatten(root.right)
            tmp = root.right
            curr = root.right = root.left
            while curr.right:
                curr = curr.right
            curr.right = tmp
            root.left = None
        elif root.right:
            self.flatten(root.right)