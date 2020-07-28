#include <bits/stdc++.h>
using namespace std;

int xC[200000],
    yC[200000];

int main() {
    // freopen("sample.in", "r", stdin);
    ios::sync_with_stdio(false);
    int n; cin >> n;
    set< pair<int, int> > points;
    for (int i=0; i<n; i++) {
        pair<int, int> cur;
        cin >> cur.first >> cur.second;
        points.insert(cur);
    }

    long long cnt = 0;
    for (set< pair<int, int> >::iterator iter = points.begin();
        iter != points.end();
        iter++) {
        int x = iter->first;
        int y = iter->second;
        xC[x]++; yC[y]++;
    }

    for (set< pair<int, int> >::iterator iter = points.begin();
        iter != points.end();
        iter++) {
        int x = iter->first;
        int y = iter->second;
        cnt += (xC[x]-1)*(yC[y]-1);
        cnt %= 10000;
    }
    cout << cnt << endl;

    return 0;
}
