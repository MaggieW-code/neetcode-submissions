class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] != "." and board[i].count(board[i][j]) > 1):
                    return False

        n = {}
        for x in range(len(board[0])):
            n[x] = []
            for y in range(len(board)):
                n[x].append(board[y][x])
        for k, column in n.items():
            for v in column:
                if (v != "." and column.count(v) > 1):
                    return False

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                box = []
                for a in range (row, row+3):
                    for b in range (col, col+3):
                        box.append(board[a][b])
                for w in box:
                    if (w != "." and box.count(w) > 1):
                        return False
        
        return True