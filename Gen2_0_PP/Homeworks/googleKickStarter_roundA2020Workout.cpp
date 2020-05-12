#include <bits/stdc++.h>
#define IOS ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define deb(x) cout << #x << " " << x << endl;
#define fi(i,a,b) for(int i = a; i<b; i++)
#define ll long long int
#define pii pair<int, int>
#define f first
#define s second
#define vi vector<int>
#define N 1000000007
#define endl "\n"
#define pb push_back
#define mp make_pair
using namespace std;

//*************************************************************************************

bool counter(ll a[], ll n, ll k, ll c)
{
	fi(i, 1, n)
	{
		ll temp = a[i] - a[i - 1];
		if (temp % k) {temp /= k;}
		else {temp /= k; temp--;}
		c -= temp; if (c < 0) {return false;}
	}
	if (c < 0) {return false;}
	return true;
}

void solve() {

	ll n, k, max_val = 0; cin >> n >> k; ll arr[n];
	fi(i, 0, n) {cin >> arr[i];}

	fi(i, 1, n) {max_val = max(max_val, arr[i] - arr[i - 1]);}

	ll l = 1, h = max_val, mid;

	while (l <= h)
	{
		mid = (l + h) / 2;

		bool ok = counter(arr, n, mid, k);

		if (ok)
		{
			if (mid == 1 || !counter(arr, n, mid - 1, k)) {cout << mid << endl; return;}
			else {h = mid - 1;}
		}
		else {l = mid + 1;}
	}
	cout << mid << endl;
}

int main() {

// #ifndef ONLINE_JUDGE
// 	freopen("input1.txt", "r", stdin);
// 	freopen("output.txt", "w", stdout);
// #endif
	IOS;

	int t; cin >> t;
	fi(i, 0, t) {cout << "Case #" << i + 1 << ": "; solve();}
	return 0 ;
}
