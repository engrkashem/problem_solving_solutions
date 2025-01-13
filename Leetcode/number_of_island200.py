class Solution:
    def numIslands(self, grid):
        result = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = {}
        row, col = len(grid), len(grid[0])

        def isInside(x, y):
            if x in range(row) and y in range(col):
                return True
            return False

        def isVisited(x, y):
            return visited.get((x, y), 0)

        def dfs(x, y):
            visited[(x, y)] = 1
            for dirX, dirY in directions:
                newX, newY = x + dirX, y + dirY
                if isInside(newX, newY) and grid[newX][newY] == "1" and not isVisited(newX, newY):
                    dfs(newX, newY)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and not isVisited(i, j):
                    result += 1
                    dfs(i, j)

        return result


obj = Solution()
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
# grid = [
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]
# ]
# grid = [
#     ["0", "1", "0"],
#     ["1", "0", "1"],
#     ["0", "1", "0"]
# ]
print(obj.numIslands(grid))


# class Solution:
#     def numIslands(self, grid):
#         result = 0
#         directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#         visited = set()
#         row, col = len(grid), len(grid[0])

#         def isInside(x, y):
#             if x in range(row) and y in range(col):
#                 return True
#             return False

#         def dfs(x, y):
#             visited.add((x, y))
#             for dirX, dirY in directions:
#                 newX, newY = x + dirX, y + dirY
#                 if isInside(newX, newY) and grid[newX][newY] == "1" and (newX, newY) not in visited:
#                     dfs(newX, newY)

#         for i in range(row):
#             for j in range(col):
#                 if grid[i][j] == "1" and (i, j) not in visited:
#                     result += 1
#                     dfs(i, j)

#         return result
