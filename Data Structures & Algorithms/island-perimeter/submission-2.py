class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
        # there is exactly one island (i.e., one or more connected land cells).
        # Return the perimeter of the island.
        # Grid cells are connected horizontally/vertically (not diagonally). 

        def get_bottom(top, bot):
            top_row = grid[top]
            occ = top_row.count(1)

            if bot >= len(grid):
                return occ
            else:
                bot_row = grid[bot]
                return sum([0 if top_row[i] == bot_row[i] else 1 for i in range(len(top_row)) ])

        def get_lr(row):
            set_counter = 0
            is_one = False
            for val in row:
                if val == 1:
                    if not is_one:
                        is_one = True
                        set_counter += 1
                else:
                    is_one = False
            return set_counter * 2

        perimeter = 0
        m = len(grid[0])
        for i, g_val in enumerate(grid):
            occ = g_val.count(1)

            if i == 0: #top row
                perimeter += occ + get_lr(g_val) + get_bottom(i, i+1)
            
            else:
                perimeter += get_lr(g_val) + get_bottom(i, i+1)

            print(perimeter)
        return perimeter


