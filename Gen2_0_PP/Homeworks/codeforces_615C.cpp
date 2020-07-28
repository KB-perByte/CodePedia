#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define CLR(a,b) memset(a,(b),sizeof(a))
#define ls st<<1
#define rs st<<1|1

const int INF = 0x3f3f3f3f;
const int MAXN = (int)2e5+10;
const int mod = (int)1e9+7;

int arr[MAXN];
map<int, int> mp;
int a[MAXN], b[MAXN], c[MAXN];

int main() {
    int n, x, y;
    cin >> n;
    map<pair<int,int>, int> mp;
    map<int, int> a, b;
    ll ans = 0;
    for(int i = 0; i < n; ++i) {
        cin >> x >> y;
        ans -= mp[{x,y}];
        mp[{x,y}]++;
        ans += a[x];
        ans += b[y];
        a[x]++;
        b[y]++;
    }
    cout << ans << endl;
    return 0;
}