"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        clone = Node(node.val)
        visited = {clone.val: {"node":clone, "child":False}}
        curr = clone
        q = deque()
        q.append(node)
        while q:
            node = q.popleft()
            for x in node.neighbors:
                if x.val not in visited:
                    visited[x.val] = {"node": Node(x.val), "child":False}
                    q.append(x)
                tmp = visited[node.val]["node"].neighbors
                tmp.append(visited[x.val]["node"])
                visited[node.val]["node"].neighbors = tmp
            visited[node.val]["child"] = True
        return clone