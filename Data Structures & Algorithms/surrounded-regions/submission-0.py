class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # dfs from border O to find which O not to flip
        unsurrounded = set()
        rows, cols = len(board), len(board[0])
        def dfs(i, j):
            if board[i][j] == 'O':
                unsurrounded.add((i,j))
                for nr, nc in [(i+1, j), (i - 1, j), (i, j+1), (i, j-1)]:
                    if (0 <= nr < rows and 
                        0 <= nc < cols and 
                        board[nr][nc] == 'O' and 
                        not (nr, nc) in unsurrounded):
                        dfs(nr, nc)
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
        print(unsurrounded)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and not (r, c) in unsurrounded:
                    board[r][c] = 'X'

        

