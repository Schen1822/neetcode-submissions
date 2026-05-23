from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        greatestArea = 0
        rows, cols = len(grid), len(grid[0])
        def findIslandArea(i: int, j: int):
            offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            queue = deque([(i, j)])
            grid[i][j] = 0
            area = 1
            while queue:
                r, c = queue.pop()
                for offset in offsets:
                    nr, nc = r + offset[0], c + offset[1]
                    if nr >= 0 and nc >= 0 and nr < rows and nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        area += 1
                        queue.append((nr, nc))
            return area
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    greatestArea = max(greatestArea, findIslandArea(row, col))
        return greatestArea
        