class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if grid == None or len(grid) == 0:
            return 0

        number_of_islands = 0

        for i, val1 in enumerate(grid):
            for j, val2 in enumerate(val1):
                if val2 == "1":
                    number_of_islands += self.get_island(i, j, grid)
        return number_of_islands

    def get_island(self, i, j, grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
            return 0

        grid[i][j] = "0"

        self.get_island(i, j - 1, grid)
        self.get_island(i, j + 1, grid)
        self.get_island(i - 1, j, grid)
        self.get_island(i + 1, j, grid)

        return 1

s = Solution()
print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))