class Solution {
public:
    string removeOuterParentheses(string S) {
        int left = 0;
        bool initialSearch = true;
        string ret = "";
        for (int ii = 0; ii < S.length(); ++ii) {
            if (initialSearch) {
                initialSearch = false;
            }
            else if (left == 0) {
                if (S[ii] == '(') {
                    ++left;
                    ret += '(';
                }
                else {
                    initialSearch = true;
                }
            }
            else {
                if (S[ii] == '(') {
                    ++left;
                    ret += '(';
                } 
                else if (S[ii] == ')') {
                    --left;
                    ret += ')';
                } 
            }
        }
        return ret;
    }
};
