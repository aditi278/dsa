# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelCountSum(self, root, height=0, m=None):
        if m == None:
            m = {} #{'0': {count, sum}}
        if root is None:
            return m
        if height in m.keys():
            m[height]['count']+=1
            m[height]['valsum']+=root.val
        else:
            m[height]= {'count': 1, 'valsum': root.val}

        self.levelCountSum(root.left, height+1, m)
        self.levelCountSum(root.right, height+1, m)

        return m
    
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        m = self.levelCountSum(root)
        arr = [0]*len(m)
        for k, v in m.items():
            arr[k]=v['valsum']/v['count']
        return arr