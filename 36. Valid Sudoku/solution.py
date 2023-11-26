class Solution:
    def checkBoxes(self, board):
        for x in range(3):
            for y in range(3):
                row = x * 3
                col = y * 3
                seen = []
                for ii in range(3):
                    for jj in range(3):
                        if board[row+ii][col+jj] in seen and board[row+ii][col+jj] != '.':
                            return False
                        else:
                            seen.append(board[row+ii][col+jj])
        return True

    def checkRows(self, board):
        for row in range(len(board)):
            seen = []
            for column in range(len(board)):
                if board[row][column] in seen and board[row][column] != '.':
                    return False
                else:
                    seen.append(board[row][column])
        return True

    def checkColumns(self, board):
        for column in range(len(board)):
            seen = []
            for row in range(len(board)):
                if board[row][column] in seen and board[row][column] != '.':
                    return False
                else:
                    seen.append(board[row][column])
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = self.checkBoxes(board)
        rows = self.checkRows(board)
        columns = self.checkColumns(board)
        return boxes and rows and columns
