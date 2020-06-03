class Solution {
public:
    string reformat(string s) {
        string alphas = "";
        string nums = "";
        if (s.length() <= 1) {
            return s;
        }
        for (int ii = 0; ii < s.length(); ++ii) {
            if (isdigit(s[ii])) {
                nums += s[ii];
            }
            else {
                alphas += s[ii];
            }
        }
        string s1 = "";
        string s2 = "";
        if (alphas.length() >= nums.length()) {
            s1 = alphas;
            s2 = nums;
        }
        else {
            s1 = nums;
            s2 = alphas;
        }
        string ret = "";
        for (int jj = 0; jj < s2.length(); ++jj) {
            ret += s1[jj];
            ret += s2[jj];
            if (jj == (s2.length() - 1) && s2.length() < s1.length()) {
                ret += s1[jj + 1];
            }
        }
        return ret;
    }
};
