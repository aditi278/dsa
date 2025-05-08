# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, root, count=0):
        if root is None:
            return 0
        count = self.getHeight(root.left)
        return count + 1
    
    def rnodes(self, root, height, count=0):
        if root is None or height == 1:
            return 0
        if root.left is None:
            return 2
        elif root.right is None:
            return 1
        elif height == 2:
            return 0
        val = self.rnodes(root.right, height - 1)
        if val:
            count += val 
        else:
            return count
        val = self.rnodes(root.left, height - 1)
        if val:
            count += val
        else:
            return count
        return count
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        height = self.getHeight(root)
        return 2**height-self.rnodes(root, height)-1
        