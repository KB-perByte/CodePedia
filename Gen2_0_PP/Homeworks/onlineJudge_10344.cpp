#include <bits/stdc++.h>
#define IOS ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define deb(x) cout << #x << " " << x << endl;
#define PI 3.14159265358979323846264338327950L
#define fi(i,a,b) for(int i = a; i<b; i++)
#define all(x) x.begin(),x.end()
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

//*************************************************************************************

static void func(vector<ll>& arr, ll val, int cnt, bool& flag)
{
	if (cnt == 5 || flag)
	{
		if (val == 23) {flag = true;}
		return;
	}

	for (int i = 0; i < 5; i++)
	{
		if (arr[i] < 0) {continue;}
		ll temp = arr[i];
		arr[i] = -1;
		func(arr, val - temp, cnt + 1, flag);
		if (flag) {return;}
		func(arr, temp + val, cnt + 1, flag);
		if (flag) {return;}
		func(arr, temp * val, cnt + 1, flag);
		if (flag) {return;}
		arr[i] = temp;
	}
}

int main() {

	IOS;

	int t = 1;
	while (true)
    {
        vector<ll> arr(5); int cnt = 0;
        fi(i, 0, 5) {cin >> arr[i]; if (arr[i] == 0) {cnt++;}}

        if (cnt == 5) {break;}

        bool flag = false;

        for (int j = 0; j < 5; j++)
        {
            ll old_val = arr[j];
            arr[j] = -1;
            func(arr, old_val, 1, flag);
            arr[j] = old_val;
            if (flag) {break;}
        }

        if (flag) {cout << "Possible" << endl;}
        else {cout << "Impossible" << endl;}
    }

	return 0 ;
}
