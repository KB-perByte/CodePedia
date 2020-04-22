#include <bits/stdc++.h>
#define LL long long
using namespace std;
const int MAXN = 200;
int happiness = 0;
LL n,m,a[MAXN],total[MAXN];
int main()
{
    cin >> n >> m;
    for (int i = 1;i <= n;i++)
    {
        cin >> a[i];
    }
    for (int i = 1;i <= n;i++)
    {
        total[i] = total[i-1]+a[i];
    }
    LL res = 0;
    for (int i = 1;i <= m;i++)
    {
        int l,r;
        cin >> l >> r;
        int happiness = total[r]-total[l-1];
        if (happiness >0)
            res += happiness;
    }
    cout << res;
    cout << endl;
    return 0;
}