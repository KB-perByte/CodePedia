#include <iostream>
#include<bits/stdc++.h>
using namespace std;
#define ll long long int
ll vec[100010];
ll K;
void mergeSort(ll L, ll R) {
    if (K < 1 || L+1 == R)
        return;
    K = K - 2;
    ll mid = (L+R)/2;
    swap(vec[mid-1], vec[mid]);
    mergeSort(L, mid);
    mergeSort (mid, R);
}
int main() {
	// your code goes here
	ll N;
	cin >> N >> K;
	if (K%2 == 0) {
	    cout << "-1" << endl;
	}
	else {
	    ll num = 1;
	    for (ll i = 0; i < N; i++) {
	        vec[i] = num;
	        num++;
	    }
	    --K;
	    mergeSort(0, N);
	    if (K)
	        cout << "-1" << endl;
	    else {
	    for (int i = 0; i < N; i++) {
	        cout << vec[i] << " ";
	    }
	    }
	}
	return 0;
}
