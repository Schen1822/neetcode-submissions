from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31-1
        rows, cols = len(grid), len(grid[0])
        offsets = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))
        while queue:
            r, c = queue.popleft()
            val = grid[r][c]
            for offset in offsets:
                nr, nc = r + offset[0], c + offset[1]
                if (
                    0 <= nr < rows and 
                    0 <= nc < cols 
                    and grid[nr][nc] == INF 
                    ):
                    queue.append((nr, nc))
                    grid[nr][nc] = val + 1
