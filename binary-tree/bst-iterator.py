# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.head = Node(-1)
        curr = self.head
        
        def parseTree(root, curr):
            if root is None:
                return curr
            curr = parseTree(root.left, curr)
            curr.next = Node(root.val)
            curr = curr.next
            return parseTree(root.right, curr)

        parseTree(root, curr)


    def next(self) -> int:
        val = self.head.next.val
        self.head.next = self.head.next.next
        return val

    def hasNext(self) -> bool:
        return True if self.head.next else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()