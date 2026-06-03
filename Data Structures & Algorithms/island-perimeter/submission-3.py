class Solution:
    def get_bottom(self, grid, a, b):
        n = len(grid[a])
        if b >= len(grid):
            return grid[a].count(1)
        return sum([0 if grid[a][i] == grid[b][i] else 1 for i in range(n)])

    def get_lr(self, row):
        is_one = False
        lr_count = 0

        for val in row:
            if val == 1:
                if is_one == False:
                    is_one = True
                    lr_count += 1
            else:
                is_one = False
        return lr_count * 2 

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
        # there is exactly one island (i.e., one or more connected land cells).
        # Return the perimeter of the island.
        # Grid cells are connected horizontally/vertically (not diagonally). 

        perimeter = 0
        for i, row in enumerate(grid):
            if i == 0:
                perimeter += row.count(1) + self.get_lr(row) + self.get_bottom(grid, i, i+1)
            else:
                a =  self.get_lr(row) 
                b =  self.get_bottom(grid, i, i+1)
                print(a)
                perimeter += (a + b)
        
        return perimeter

