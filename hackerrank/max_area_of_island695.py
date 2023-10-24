class Solution(object):
    def maxAreaOfIsland(self, grid):
        largest_island = 0
        visited = set()
        rowNo, colNo = len(grid), len(grid[0])
        direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def isInside(node):
            if node[0] >= 0 and node[0] < rowNo and node[1] >= 0 and node[1] < colNo:
                return True
            return False

        def dfs(node, area):
            visited.add(node)
            area += 1
            x = node[0]
            y = node[1]

            for x1, y1 in direction:
                newX = x+x1
                newY = y+y1
                newNode = (newX, newY)

                if isInside(newNode) and newNode not in visited and grid[newX][newY] == 1:
                    area = dfs(newNode, area)
            return area

        # find unvisited island and measure area of island. calculate largest island
        for row in range(rowNo):
            for col in range(colNo):
                if grid[row][col] == 1 and (row, col) not in visited:
                    # visited.add((row,col))
                    area = dfs((row, col), 0)
                    largest_island = max(largest_island, area)
                    # current_no_island = 0
        return largest_island


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

# grid = [[0, 0, 0, 0, 0, 0, 0, 0]]

obj = Solution()
print(obj.maxAreaOfIsland(grid))
