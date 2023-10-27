class Solution(object):
    def solve(self, board):
        n, m = len(board), len(board[0])
        isSorroundedRegion = [True]
        visited = set()
        direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def isInside(node):
            if node[0] >= 0 and node[0] < n and node[1] >= 0 and node[1] < m:
                return True
            return False

        def checkSorroundingCell(node):
            if node[0] == 0 or node[1] == 0 or node[0] == n-1 or node[1] == m-1:
                return True
            return False

        def dfs(node, flag):
            visited.add(node)
            x = node[0]
            y = node[1]

            if checkSorroundingCell(node):
                isSorroundedRegion[0] = False
                return

            board[x][y] = flag

            for dx, dy in direction:
                newX = x+dx
                newY = y+dy
                newNode = (newX, newY)

                if isInside(newNode) and newNode not in visited and board[newX][newY] != 'X':
                    dfs(newNode, flag)

        for i in range(n):
            for j in range(m):
                if board[i][j] != 'X':
                    dfs((i, j), board[i][j])
                    visited.clear()

                    if isSorroundedRegion[0]:
                        dfs((i, j), 'X')
                    isSorroundedRegion[0] = True
                    visited.clear()
        return board


obj = Solution()

# board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
#          ["X", "X", "O", "X"], ["X", "O", "X", "X"]]

# board = [["X"]]

board = [["O", "X", "X", "O", "X"],
         ["X", "O", "O", "X", "O"],
         ["X", "O", "X", "O", "X"],
         ["O", "X", "O", "O", "O"],
         ["X", "X", "O", "X", "O"]]

expOp = [["O", "X", "X", "O", "X"],
         ["X", "X", "X", "X", "O"],
         ["X", "X", "X", "O", "X"],
         ["O", "X", "O", "O", "O"],
         ["X", "X", "O", "X", "O"]]

print(obj.solve(board))
