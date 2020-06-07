#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
 
const int INF = 0x3f3f3f3f;
const int MAXN = 1.5e7 + 10;
int pri[MAXN], a[MAXN];
 
int gcd(int a, int b)
{
	if (!b)
		return a;
	return gcd(b, a % b);
}
int main()
{
#ifdef LOCAL
	freopen("C:/input.txt", "r", stdin);
#endif
	int n, g = 0;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		int t;
		scanf("%d", &t);
		a[t]++;
		if (!g)
			g = t;
		else
			g = gcd(g, t);
	}
	int ans = n;
	for (int i = g + 1; i < MAXN; i++) 
		if (!pri[i])
		{
			int cnt = 0, j;
			for (j = i; j < MAXN; j += i)
				pri[j] = 1, cnt += a[j];
			ans = min(ans, n - cnt);
		}
	if (ans < n)
		cout << ans << endl;
	else
		cout << -1 << endl;
 
	return 0;
}