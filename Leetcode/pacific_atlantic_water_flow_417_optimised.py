class Solution(object):
    def pacificAtlantic(self, heights):
        n, m = len(heights), len(heights[0])
        atlanticTouched = [False]
        pacificTouched = [False]
        output = []
        visited = set()
        direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        memory = set()

        def isInside(node):
            if node[0] >= 0 and node[0] < n and node[1] >= 0 and node[1] < m:
                return True
            return False

        def dfs(node):
            visited.add(node)
            x = node[0]
            y = node[1]

            if x == 0 or y == 0:
                pacificTouched[0] = True

            if x == n-1 or y == m-1:
                atlanticTouched[0] = True

            if node in memory:
                pacificTouched[0] = True
                atlanticTouched[0] = True

            if atlanticTouched[0] and pacificTouched[0]:
                return True

            for x1, y1 in direction:
                newX = x+x1
                newY = y+y1
                newNode = (newX, newY)

                if isInside(newNode) and newNode not in visited and heights[x][y] >= heights[newX][newY]:
                    dfs(newNode)

            return False

        for i in range(n):
            for j in range(m):
                if (i == 0 or j == 0) and (i == n-1 or j == m-1):
                    output.append([i, j])
                    continue

                dfs((i, j))
                if atlanticTouched[0] and pacificTouched[0]:
                    output.append([i, j])
                    memory.add((i, j))
                atlanticTouched[0] = False
                pacificTouched[0] = False
                visited.clear()

        return output


obj = Solution()

heights = [[1, 2, 2, 3, 5],
           [3, 2, 3, 4, 4],
           [2, 4, 5, 3, 1],
           [6, 7, 1, 4, 5],
           [5, 1, 1, 2, 4]]

# heights = [[1]]

print(obj.pacificAtlantic(heights))
