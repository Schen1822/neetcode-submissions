"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        cloned = {}
        cloned[node.val] = Node(node.val, None)
        startNode = cloned[node.val]
        queue = deque([node])
        while queue:
            curr = queue.popleft()
            currentNode = cloned[curr.val]
            for neighbor in curr.neighbors:
                visited = cloned.get(neighbor.val, None)
                if not visited:
                    neighborNode = Node(neighbor.val, None)
                    queue.append(neighbor)
                    currentNode.neighbors.append(neighborNode)
                    cloned[neighbor.val] = neighborNode
                else:
                    currentNode.neighbors.append(cloned[neighbor.val])
        return startNode


        