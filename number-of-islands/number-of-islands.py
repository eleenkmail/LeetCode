class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If a cell with value 1 is not visited yet,
                # then new island found
                if grid[i][j] == "1":
                    # Visit all cells in this island
                    # and increment island count
                    self.DFS(i, j, grid)
                    count += 1
 
        return count


    def DFS(self, i, j, grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
            return

        grid[i][j] = "-1"
 
        
        self.DFS(i - 1, j, grid)
        self.DFS(i + 1, j, grid)
        self.DFS(i, j - 1, grid)
        self.DFS(i, j + 1, grid)
        
 
        
        


