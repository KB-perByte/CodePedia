#include <cstdio>
#include <cstring>
#include <iostream>
 
using namespace std;
 
const int maxn = 15, lim = 1024;
int has[maxn][maxn], n;

void fill(int r, int c, int lft) {
	if (r > n) return ;
	has[r][c] += lft;
 
	if (has[r][c] > lim) {
		int left = has[r][c] - lim;
		has[r][c] = lim; 
		fill(r + 1, c, left / 2);
		fill(r + 1, c + 1, left / 2);
	}
}
 
int main()
{
	int t;
	cin >> n >> t;
	memset(has, 0, sizeof(has));
	while(t--) {
		fill(1, 1, lim);
	}
	int ans = 0;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			ans += has[i][j] == lim;
		}
	}
	cout << ans << endl;
	return 0;
}