class Solution {
public:
    static bool inSquare(int ii, int jj, vector<vector<char>> board, char c) {
        int x, y;
        if (ii < 3) {
            y = 0;
        }
        else if (ii < 6) {
            y = 3;
        }
        else if (ii < 9) {
            y = 6;
        }
        if (jj < 3) {
            x = 0;
        }
        else if (jj < 6) {
            x = 3;
        }
        else if (jj < 9) {
            x = 6;
        }
        
        for (int kk = 0; kk < 3; kk++) {
            for (int ll = 0; ll < 3; ll++) {
                if (board[y + kk][x + ll] == c) {
                    return true;
                }
            }
        }
        return false;
    }
    
    static bool contains(vector<char> list, char c) {
        for (char item:list) {
            if (c == item) {
                return true;
            }
        }
        return false;
    }
    
    static bool isSolved(vector<vector<char>> board) {
        for (int ii = 0; ii < 9; ii++) {
            for (int jj = 0; jj < 9; jj++) {
                if (board[ii][jj] == '.') {
                    return false;
                }
            }
        }
        return true;
    }
    
    static int tryToFillSquare(int ii, int jj, vector<vector<char>> leftToRight, vector<vector<char>> topDown) {
        bool couldFill = true;
        vector<char> otn = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};
        vector<int> valid;
        
        // Check if there is only one option to go in this spot.
        for (int kk = 0; kk < 9; kk++) {
            if (!contains(leftToRight[ii], otn[kk]) && !contains(topDown[jj], otn[kk])  && !inSquare(ii, jj, leftToRight, otn[kk])) {
                valid.push_back(kk + 1);
            }
        }
        if (valid.size() == 1) {
            return valid[0];
        }
        
        if (!couldFill) {
            return -1;
        }
        return 0;
    }
    
    // Helper to turn the board on its side.
    static vector<vector<char>> turn(vector<vector<char>> in) {
        vector<char> tmp;
        vector<vector<char>> out;
        for (int ii = 0; ii < 9; ii++) {
            tmp.clear();
            for (int jj = 0; jj < 9; jj++) {
                tmp.push_back(in[jj][ii]);
            }
            out.push_back(tmp);
        }
        return out;
    }
    
    void solveSudoku(vector<vector<char>>& board) {
        vector<vector<char>> leftToRight = board;
        // Top down to avoid excess vector traversal.
        vector<vector<char>> topDown = turn(board);
        vector<char> otn = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '8'};
        bool solved = false;
        
        int tmp = -1;
        while (!solved) {
            
            for (int ii = 0; ii < 9; ii++) {
                for (int jj = 0; jj < 9; jj++) {
                    if (leftToRight[ii][jj] == '.') {  
                        // If tmp == -1 after this, it could not be filled.
                        tmp = tryToFillSquare(ii, jj, leftToRight, topDown);
                        if (tmp != -1) {
                            leftToRight[ii][jj] = otn[tmp + 1];
                            topDown[jj][ii] = otn[tmp + 1];
                        }
                    }
                }
            }
            solved = isSolved(leftToRight);
        }
        board = leftToRight;
    }
};
