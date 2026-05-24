from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()
        minutes = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
        while queue:
            r, c, ts = queue.popleft()
            minutes = max(minutes, ts)
            for offset in offsets:
                nr, nc = r + offset[0], c + offset[1]
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, ts + 1))
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        return minutes


