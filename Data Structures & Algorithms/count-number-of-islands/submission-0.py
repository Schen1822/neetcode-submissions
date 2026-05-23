from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        cols, rows = len(grid[0]), len(grid)
        count = 0
    
        def searchIsland(i: int, j: int):
            offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            queue = deque([(i,j)])
            grid[i][j] = '0'
            while queue:
                r, c = queue.popleft()
                for offset in offsets:
                    nr, nc = r + offset[0], c + offset[1]
                    if nr >= 0 and nc >= 0 and nr < rows and nc < cols and grid[nr][nc] == '1':
                        queue.append((nr, nc))
                        grid[nr][nc] = '0'
            return
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    searchIsland(row, col)
                    count += 1
        return count