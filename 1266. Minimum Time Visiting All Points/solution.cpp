class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        int currx = points[0][0];
        int curry = points[0][1];
        int nextx, nexty, total, xdiff, ydiff = 0;
        int ii = 1;
        
        while (ii < points.size()) {
            nextx = points[ii][0];
            nexty = points[ii][1];
            xdiff = abs(nextx - currx);
            ydiff = abs(nexty - curry);
            if (xdiff >= ydiff) {
                total += xdiff;
            }
            else {
                total += ydiff;
            }
            currx = nextx;
            curry = nexty;
            ii++;
        }
        return total;
    }
};
