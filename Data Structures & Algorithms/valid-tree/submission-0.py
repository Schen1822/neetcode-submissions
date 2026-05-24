from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        visited = [False] * n
        if len(edges) != n - 1:
            return False

        def find_cycle(node, parent):
            print(node, parent)
            visited[node] = True
            neighbors = adj[node]
            for n in neighbors:
                if not visited[n]:
                    return find_cycle(n, node)
                elif n != parent and parent >= 0:
                    print("cycle detected", n, parent)
                    return True
            return False

        for node in range(n):
            if not visited[node]:
                if find_cycle(node, -1):
                    print("cycle found starting from ", node)
                    return False
        return True

        