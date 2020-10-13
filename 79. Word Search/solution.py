class Solution(object):
    def verify_rest(self, board, restword, coords):
        curr_letter = restword[0]
        x = coords[0]
        y = coords[1]
        if x > 0 and board[y][x - 1] == curr_letter:
            if len(restword) == 1:
                return True
            return self.verify_rest(board, restword[1:], (x - 1, y))
        if x < len(board[0]) - 1 and board[y][x + 1] == curr_letter:
            if len(restword) == 1:
                return True
            return self.verify_rest(board, restword[1:], (x + 1, y))
        if y > 0 and board[y - 1][x] == curr_letter:
            if len(restword) == 1:
                return True
            return self.verify_rest(board, restword[1:], (x, y - 1))
        if y < len(board) - 1 and board[y + 1][x] == curr_letter:
            if len(restword) == 1:
                return True
            return self.verify_rest(board, restword[1:], (x + 1, y))
        return False
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ycoord = 0
        xcoord = 0
        starting_letter = word[0]
        for line in board:
            xcoord = 0
            for letter in line:
                if letter == starting_letter:
                    if self.verify_rest(board, word[1:], (xcoord, ycoord)):
                        return True
                xcoord += 1
            ycoord += 1
        # If there is no return before here, the board doesn't contain the word.
        return True
