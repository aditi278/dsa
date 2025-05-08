# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root, s=None):
        if s is None:
            s = []
        if root is None:
            return s.append('None')
        self.preorder(root.left, s)
        s.append(root.val)
        self.preorder(root.right, s)
        return s

    def postorder(self, root, s=None):
        if s is None:
            s = []
        if root is None:
            return s.append('None')
        self.postorder(root.right, s)
        s.append(root.val)
        self.postorder(root.left, s)
        return s
    
    def inorderleft(self, root, s=None):
        if s is None:
            s = []
        if root is None:
            return s.append('None')
        s.append(root.val)
        self.inorderleft(root.left, s)
        self.inorderleft(root.right, s)
        return s
    
    def inorderright(self, root, s=None):
        if s is None:
            s = []
        if root is None:
            return s.append('None')
        s.append(root.val)
        self.inorderright(root.right, s)
        self.inorderright(root.left, s)
        return s
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if self.preorder(root.left) != self.postorder(root.right) or self.inorderleft(root.left) != self.inorderright(root.right):
            return False
        return True