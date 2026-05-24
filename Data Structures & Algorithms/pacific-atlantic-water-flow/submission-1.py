class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic, pacific = set(), set()
        rows, cols = len(heights), len(heights[0])
        def dfs(i, j, prev, reached):
            if i < 0 or i >= rows or j < 0 or j >= cols or heights[i][j] < prev or (i, j) in reached:
                return
            else:
                reached.add((i, j))
                dfs(i+1, j, heights[i][j], reached)
                dfs(i-1, j, heights[i][j], reached)
                dfs(i, j+1, heights[i][j], reached)
                dfs(i, j-1, heights[i][j], reached)
        
        for row in range(rows):
            dfs(row, 0, heights[row][0], pacific)
            dfs(row, cols - 1, heights[row][cols - 1], atlantic)
        for col in range(cols):
            dfs(0, col, heights[0][col], pacific)
            dfs(rows - 1, col, heights[rows - 1][col], atlantic)
        return list(pacific.intersection(atlantic))
        