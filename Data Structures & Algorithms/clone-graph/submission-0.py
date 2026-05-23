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
        visited = set() # contains all visited values
        clonedNodes = {}
        clonedNodes[node.val] = Node(node.val, None)
        startNode = clonedNodes[node.val]
        queue = deque([node])
        while queue:
            curr = queue.popleft()
            currentNode = clonedNodes[curr.val]
            for neighbor in curr.neighbors:
                if not neighbor.val in visited:
                    neighborNode = Node(neighbor.val, None)
                    queue.append(neighbor)
                    visited.add(neighbor.val)
                    currentNode.neighbors.append(neighborNode)
                    clonedNodes[neighbor.val] = neighborNode
                else:
                    currentNode.neighbors.append(clonedNodes[neighbor.val])
        return startNode


        