# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode], level=0, out=None) -> List[List[int]]:
        if out is None:
            out = []
        if root is None:
            return out
        if len(out) - 1 < level:
            out.append([root.val])
        else:
            l = out[level]
            l.append(root.val)
            out[level] = l
        self.levelOrder(root.left, level+1, out)
        self.levelOrder(root.right, level+1, out)
        return out