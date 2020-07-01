#include <bits/stdc++.h>
#define Acc ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define deb(x) cout << #x << " " << x << endl;
#define fi(i,a,b) for(int i = a; i<b; i++)
#define ull unsigned long long
#define all(x) x.begin(), x.end()
#define ll long long int
#define ld long double
#define pii pair<int, int>
#define F first
#define S second
#define vi vector<int>
#define N 1000000007
#define endl "\n"
#define pb push_back
#define mp make_pair
using namespace std;


void solve() {

	ll n, k, sum = 0; cin >> n >> k; vector<ll> arr(n + 1);
	fi(i, 1, n + 1) {cin >> arr[i];}

	int i = 1, j = 1;
	while (j < n + 2) {

		if (sum == k) {cout << i << " " << j - 1 << endl; return;}
		else if (sum < k) {sum += arr[j]; j++;}
		else {sum -= arr[i]; i++;}
	}
	cout << -1 << endl;
}

int main() {

	Acc;

	int t = 1; cin >> t;
	fi(i, 0, t) {solve();}
	return 0 ;
}
