class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // To house the up down and side to side lines as well as the 3x3 segments.
        vector<vector<char>> segments;
        
        // Check if board is 9x9.
        if (board.size() != 9) {
            return false;
        }
        for (auto line:board) {
            if (line.size() != 9) {
                return false;
            }
        }
        
        // Add L->R and T->B segments.
        vector<char> tmp1;
        vector<char> tmp2;
        for (int ii = 0; ii < 9; ii++) {
            tmp1.clear();
            tmp2.clear();
            for (int jj = 0; jj < 9; jj++) {
                if (board[ii][jj] != '.') {
                    tmp1.push_back(board[ii][jj]);
                }
                if (board[jj][ii] != '.') {
                    tmp2.push_back(board[jj][ii]);
                }
            }
            segments.push_back(tmp1);
            segments.push_back(tmp2);
        }
        
        // Add the 3x3 segments.
        vector<char> tmp3;
        for (int kk = 0; kk < 3; kk++) {
            for (int ll = 0; ll < 3; ll++) {
                tmp3.clear();
                for (int mm = 0; mm < 3; mm++) {
                    if (board[(kk * 3) + mm][(ll * 3)] != '.') {
                        tmp3.push_back(board[(kk * 3) + mm][(ll * 3)]);
                    }
                    if (board[(kk * 3) + mm][(ll * 3) + 1] != '.') {
                        tmp3.push_back(board[(kk * 3) + mm][(ll * 3) + 1]);
                    }
                    if (board[(kk * 3) + mm][(ll * 3) + 2] != '.') {
                        tmp3.push_back(board[(kk * 3) + mm][(ll * 3) + 2]);
                    }
                }
                segments.push_back(tmp3);
            }
        }
        
        // Check for all unique.
        for (int nn = 0; nn < segments.size(); nn++) {
            for (int oo = 0; oo < segments[nn].size(); oo++) {
                for (int pp = oo + 1; pp < segments[nn].size(); pp++) {
                    if (segments[nn][oo] == segments[nn][pp]) {
                        return false;
                    }
                }
            }
        }
        
        // If all went well, then it is solveable.
        return true;  
    }
};
