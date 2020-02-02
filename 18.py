class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        number_of_islands = 0

        if grid == None or len(grid) == 0:
            return 0

        for i, val1 in enumerate(grid):
            for j, val2 in enumerate(val1):
                if val2 == 0:
                    result = self.get_island(i, j, grid)
                    if result[1]:
                        number_of_islands += result[0]

        return number_of_islands

    def get_island(self, i, j, grid):

        is_closed = True

        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 1:
            return 0, is_closed


        if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1:
            is_closed = False

        grid[i][j] = 1

        is_closed *= self.get_island(i + 1, j, grid)[1]
        is_closed *= self.get_island(i - 1, j, grid)[1]
        is_closed *= self.get_island(i, j + 1, grid)[1]
        is_closed *= self.get_island(i, j - 1, grid)[1]

        return 1, is_closed


s = Solution()
print(s.closedIsland(
[[0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
 [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
 [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
 [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
 [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
 [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
 [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
 [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
 [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
 [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]))