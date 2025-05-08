# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
        i = len(nums)//2
        node = TreeNode(val=nums[i])
        if i >= 0:
            node.left = self.sortedArrayToBST(nums[:i])
        if i+1 >= 0:
            node.right = self.sortedArrayToBST(nums[i+1:])
        return node