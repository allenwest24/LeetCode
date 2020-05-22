class Solution {
public:
    string defangIPaddr(string address) {
        string ret;
        for (int ii = 0; ii < address.length(); ++ii) {
            if (address[ii] == '.') {
                ret += "[.]";
            }
            else {
                ret += address[ii];
            }
        }
        return ret;
    }
};
