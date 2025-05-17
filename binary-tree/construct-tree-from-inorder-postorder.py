# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        val = postorder.pop()
        root = TreeNode(val)
        if postorder == []:
            return root
        while postorder:
            child_val = postorder[-1] 
            root_ind = inorder.index(val)
            if child_val not in inorder:
                return root
            child_ind = inorder.index(child_val)
            if child_ind < root_ind:
                root.left = self.buildTree(inorder[:root_ind], postorder)
            else:
                root.right = self.buildTree(inorder[root_ind+1:], postorder)
        
        return root