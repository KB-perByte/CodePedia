
/*
input: [[2,1],[3,2],[4,3],[5,4]]
slope:    ^    1/1   1/1   1/1    Slope is dy/dx, e.g. (5-2)/(4-1)=3/3=1/1
|        o                        GCD is used to map equal slopes to identical.
|      o      result: number of identical slopes + starting point = 3+1=4
|    o 
|  o
+--------------------------

input: [[2,1],[3,2],[6,3],[5,4]]
slope:    ^    1/1   2/1   1/1    We keep track of slopes related to the 
|        o                        current point [2,1] in map.
|          o  result: number of identical slopes + starting point = 2+1=3
|    o 
|  o
+--------------------------

input: [[2,2],[3,2],[5,2],[6,2]]
slope:    ^    1/0   1/0   1/0    GCD returns dx for pair [dx, 0].
|                                 Then dx/dx / 0/dx = 1/0
|             result: 3 + 1 = 4
|  o o   o o
|  
+--------------------------

input: [[3,1],[3,2],[3,3],[3,4]]
slope:    ^    0/1   0/1   0/1    GCD retuns dy for [o,dy].
|    o                            Then 0/dy / dy/dy = 0/1
|    o        result: 3 + 1 = 4
|    o
|    o
+--------------------------

input: [[2,1],[3,2],[2,1],[4,1],[5,4],[2,1],[2,1]]
slope:    ^    1/1   dup   1/0   1/1   dup   dup
|        o                       Identical points have no slope.
|                                We have 2 possible lines: 2 * 1/1 and 1 * 1/0.
|    o                           Keep track of duplicates and add them to max line.
|  0   o      result: 3 dups + max(2,1) + 1 = 6 
+--------------------------

input: [[1,1],[5,1],[2,2],[3,3],[4,4],[6,2],[7,3]]
slope:    ^    1/0   1/1   1/1   1/1   5/1   3/1    Slopes: max(1,3,1,1) = 3
slope:          ^   -3/1   1/-1  1/-3  1/1   1/1    Slopes: max(1,1,1,2) = 2
|       o                        The map tracks slopes for the current point only.
|     o       o                  So parallel lines do not sum up points.
|   o       o         
| o       o    result: 0 dups + max(3,2) + 1 = 4 
+--------------------------
*/

class Solution {
public:
    int getGcd(const int a, const int b)
    {
        if(a==0) return b;
        return getGcd(b%a, a);
    }
    
    int maxPoints(vector<vector<int>>& points) {
        int v, res=0,len=points.size();
        if(len<3) return len;
        for(int i=0;i+res<len;i++)
        {
            unordered_map<string,int> m;
            int x1 = points[i][0], y1 = points[i][1], v=0, maxv=0, dups=0;
            int nIdentical=0;
            // start with i+1, since if any previous point is on the same line,
            // then this was already calculated then that point was a starting point
            for(int j=i+1;j<len;j++)
            {
                int x2 = points[j][0], y2 = points[j][1];
                int dx = x2-x1, dy = y2-y1;

                if(dx==0 && dy==0)
                {
                    dups++;
                }
                else
                {
                    // we need the slope: dx/dy. but float rounds up the end and produces slightly different results,
                    // so instead we keep both dx and dy as the key.
                    // to make them identical for the identical slope, use GCD: greatest common divisor
                    int gcd = getGcd(dx,dy);
                    dy/=gcd; dx/=gcd;

                    // dx and dy define the slope.
                    // we keep the map for the current point i, so the full key is point[i]+slope excludes parallel lines.
                    // vertical line: dx==0, horizontal line: dy==0. GCD will set vertical: dx=0, dy=1, horizontal: dx=1, dy=0 
                    string key = to_string(dx) + '/'+ to_string(dy);
                    if(m.find(key) != m.end()) {m[key]++; v=m[key]; }
                    else { m[key]=1; v=1; }
                }
                // duplicates should increase our best result found with point[i]
                if(maxv < v) maxv = v;
                if(res < dups + maxv + 1) res = dups + maxv + 1;
            } 
        }
        return res;
    }
};