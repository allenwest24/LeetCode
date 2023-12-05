class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Base case
        if len(grid) == 0:
            return 0

        # Counter
        out = 0

        # Go through every element
        for ii in range(len(grid)):
            for jj in range(len(grid[ii])):
                # Only care about new islands (aka 1's)
                if grid[ii][jj] == "1":
                    out += 1
                    grid = self.fill_out_island(jj, ii, grid)
        
        return out

    # DFS helper to find all parts of this island and mark them as seen ("0")
    def fill_out_island(self, x, y, grid):
        # Bounds detect
        if y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y]):
            # Only new island portions
            if grid[y][x] == "1":
                # Set as ignore
                grid[y][x] = "0"
                # Up, down, left, right
                grid = self.fill_out_island(x+1, y, grid)
                grid = self.fill_out_island(x, y+1, grid)
                grid = self.fill_out_island(x, y-1, grid)
                grid = self.fill_out_island(x-1, y, grid)
        # Return potentially updated grid
        return grid
