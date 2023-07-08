import numpy as np
class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        
        rows,cols = len(grid),len(grid[0])
        
        visited = np.zeros((rows,cols), dtype = int)

        def bfs(grid, row, col, prev_r, prev_c, value):

                start=[row, col, prev_r, prev_c]

                queue=[start]
                 
                res = []

                while queue:
                    i,j,r,c = queue.pop(0)
                    if i+1<len(grid) and grid[i+1][j]==value and [i+1,j]!=[r,c]:
                        queue.append([i+1,j,i,j])
              
                    if i-1>=0 and grid[i-1][j]==value and [i-1,j]!=[r,c]:
                        queue.append([i-1,j,i,j])

                    if j+1<len(grid[0]) and grid[i][j+1]==value and [i,j+1]!=[r,c]:
                        queue.append([i,j+1,i,j])
                        
                    if j-1>=0 and grid[i][j-1]==value and [i,j-1]!=[r,c]:    
                        queue.append([i,j-1,i,j])

                    if visited[i][j]==1:
                        return True
                    
                    res.append([i,j])
                    visited[i][j]=1

                return False


        for i in range(rows):
            for j in range(cols):
                if visited[i][j]==0 and bfs(grid,i,j,-1,-1,grid[i][j]):
                    return True
        return False




