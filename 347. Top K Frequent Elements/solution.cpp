class Solution {
public:
    // Helper to compare only the counts of the two pairs given.
    static bool comp(pair<int, int> a, pair<int, int> b) {
        return a.second > b.second;
    }
    
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Create a map.
        unordered_map<int, int> map;
        
        // Map the items in given vector and update counts.
        for (int num:nums) {
            map[num]++;
        }
        
        // Create a vector of pairs for values and counts to be sorted by counts.
        vector<pair<int, int>> toSort;
        for (auto pair:map) {
            toSort.push_back(pair);
        }
        
        // Use sort on toSort using the static pair compare helper.
        sort(toSort.begin(), toSort.end(), comp);
        
        // Make a vector of length k and then set the top count as the first element.
        vector<int> ans(k);
        for (int ii = 0; ii < k; ii++) {
            ans[ii] = toSort[ii].first;
        }
        
        return ans;
    }
};
