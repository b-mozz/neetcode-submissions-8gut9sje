class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count = 0
        
        def countIslands(r, c):
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == '0':
                return 
            #if nums[r][c] == 1
            grid[r][c] = '0'
            #go down, up, right, left: make everything connected a 0
            countIslands(r+1, c)
            countIslands(r-1, c)
            countIslands(r, c+1)
            countIslands(r, c-1)
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    countIslands(i,j)
                    count += 1
        
        return count
            




        