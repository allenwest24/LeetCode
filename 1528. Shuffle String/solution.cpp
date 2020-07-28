class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        string shuffled = s;
	    for (int ii = 0; ii < indices.size(); ii++)
		    shuffled[indices[ii]] = s[ii];
	    return shuffled;
    }
};
