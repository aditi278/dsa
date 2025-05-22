# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        arr = []
        q = [[root, 0]]
        while q:
            node, level = q.pop(0)
            if level < len(arr):
                tmp = arr[level]
                tmp.append(node.val)
                arr[level] = tmp
            else:
                arr.append([node.val])
            if node.left:
                q.append([node.left, level+1])
            if node.right:
                q.append([node.right, level+1])
        for i in range(len(arr)):
            if i%2:
                arr[i] = arr[i][::-1]

        return arr