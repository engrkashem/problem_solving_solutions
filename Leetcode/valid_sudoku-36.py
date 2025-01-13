from collections import defaultdict

def isValidSudoku(board):
    columns=defaultdict(list)
    rows=defaultdict(list)
    squares=defaultdict(list)
    
    for row in range(9):
        for col in range(9):
            if board[row][col]==".":
                continue
            
            if (board[row][col] in columns[col] or 
                board[row][col] in rows[row] or
                board[row][col] in squares[(row//3, col//3)]):
                return False
            
            columns[col].append(board[row][col])
            rows[row].append(board[row][col])
            squares[(row//3, col//3)].append(board[row][col])
    
    return True