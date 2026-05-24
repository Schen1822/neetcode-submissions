class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic = set()
        pacific = set()
        pacificIndices = set()
        atlanticIndices = set()
        # find two different sets, 
        # starting from each ocean, find reachable indices
        # return the intersection
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
            for col in range(cols):
                if row == 0:
                    pacificIndices.add((row, col))
                if row == rows - 1:
                    atlanticIndices.add((row, col))
                pacificIndices.add((row, 0))
                atlanticIndices.add((row, cols-1))
        for i, j in pacificIndices:
            dfs(i, j, 0, pacific)
        for i, j in atlanticIndices:
            dfs(i, j, 0, atlantic)
        return list(pacific.intersection(atlantic))
        