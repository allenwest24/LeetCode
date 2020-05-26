class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string> out;
        int temp = 0;
        int curr = 1;
        for (int ii = 0; ii < target.size(); ++ii) {
            temp = target[ii];
            if (temp > curr) {
                while (temp > curr) {
                    out.push_back("Push");
                    out.push_back("Pop");
                    ++curr;
                }
                out.push_back("Push");
            }
            else if (temp == curr) {
                out.push_back("Push");
            }
            ++curr;
        }
        return out;
    }
};
