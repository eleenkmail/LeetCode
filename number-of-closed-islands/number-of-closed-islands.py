class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def dfs(i, j):
            if grid[i][j] == -1:
                
                return False

            if grid[i][j] == 1:
                return True

            grid[i][j] = 1
            
            up = dfs(i-1, j)
            down = dfs(i+1, j)
            right = dfs(i, j+1)
            left = dfs(i, j-1)
            return up and down and right and left 


        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 0 and (i == 0 or i == rows-1 or j == 0 or j == cols-1):

                    grid[i][j] = -1
        
 

        count = 0

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 0:
                    if dfs(i, j):
                        count +=1
        
        return count


        