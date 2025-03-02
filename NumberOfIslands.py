# 200. Number of Islands
class Solution:

    # Function to iterate adjacent cells i.e down, right, up, left
    def helper(self,grid,i,j):
        n = len(grid)
        m = len(grid[0])
        # Base condition
        if i<0 or j<0 or i>=n or j>=m or grid[i][j]=='0':
            return

        grid[i][j] = '0'

        # Checking adjacent cells are land or not
        self.helper(grid,i+1,j) # Down
        self.helper(grid,i,j+1) # Right
        self.helper(grid,i-1,j) # Up
        self.helper(grid,i,j-1) # Left

    def numIslands(self, grid: List[List[str]]) -> int:
        # Length of row and column
        r = len(grid)
        c = len(grid[0])

        count = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    count +=1
                    self.helper(grid,i,j)
        return count
        