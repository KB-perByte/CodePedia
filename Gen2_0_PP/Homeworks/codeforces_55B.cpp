#include<bits/stdc++.h>
#define ll long long int
#define CIN ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define pb push_back
#define MOD 1000000007
#define vi vector<int>
#define vll vector<ll>
#define MID (l + (h - l) / 2)
#define all(x) x.begin(),x.end()
#define MAX =INT_MAX
#define MIN =INT_MIN
#define BS l<=r

using namespace std;

void func(vector<ll> a, vector<char> &c, ll &x, int p) {  // a is pass by value 
	if (a.size() == 1) {  //after shrinking when arr becomes size of 1
		x = min(a[0], x); //keep track of min value in all posible results		
			return;
	}
 
	for (ll i = 0; i < a.size(); i++) {   //for considering diff combinations or we are fixing ith elem to compute all its possible values with others
		for (ll j = i + 1; j < a.size(); j++) { // once i is fixed we will consider other elem for series of operations
			vector<ll> temp;            //to store the computed values and other value in each fn call
			if (c[p] == '*') {              // for series of operators
				temp.pb(a[i] * a[j]);
			}
			else if (c[p] == '+') {
				temp.pb(a[i] + a[j]);
			}
			for (int k = 0; k < i; k++){
			 temp.pb(a[k]);      // whn we picked the 2 elem then we need to store the other elem for their future consideration
			}
			for (int k = i + 1; k < j; k++) {
			temp.pb(a[k]); // considering all the cases to store other elem
			}
			for (int k = j + 1; k < a.size(); k++){ 
				temp.pb(a[k]);
			}
 
			func(temp, c, x, p + 1);   // at every fun call we will inc our p to consider other operator in next fn call
		// see recursion tree daigram for better understanding
		}
	}
}

int main()
{
	
	CIN
	vector<ll> a(4);
	vector<char> c(3);
	ll flag = 0;
	ll x = LLONG_MAX;
 
	for(int i=0;i< 4;i++){
	 cin >> a[i];
	}
	for(int i=0;i< 3;i++){
	 cin >> c[i];
	}
 
	func(a, c, x, 0);
	cout << x;

	return 0;
}