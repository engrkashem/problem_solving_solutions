class Solution(object):
    def orangesRotting(self, grid):
        queue = []
        fresh_fruit_no = 0
        resultant_time = 0
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                element = grid[i][j]
                if element == 1:
                    fresh_fruit_no += 1
                elif element == 2:
                    queue.append((i, j))

        while fresh_fruit_no and queue:
            length = len(queue)
            for i in range(length):
                row, col = queue[0]
                queue.pop(0)

                for dr, dc in direction:
                    newRow = row+dr
                    newCol = col+dc
                    if newRow in range(n) and newCol in range(m) and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        queue.append((newRow, newCol))
                        fresh_fruit_no -= 1

            resultant_time += 1

        if fresh_fruit_no:
            return -1
        else:
            return resultant_time


'''
import collections


class Solution:
    def orangesRotting(self, grid):
        q = collections.deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # if in bounds and nonrotten, make rotten
                    # and add to q
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

'''


obj = Solution()
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
# grid = [[2, 1, 1], [1, 1, 0], [0, 1, 2]]
print(obj.orangesRotting(grid))
