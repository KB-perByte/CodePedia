
#include <iostream>

#define ll long long int

using namespace std;

ll count = 0;

void merge(ll arr[], ll l, ll m, ll r);

void mergeSort(ll arr[], ll l, ll r) {
    if (l < r)   {
        int m = l+(r-l)/2;
        mergeSort(arr, l, m);
        mergeSort(arr, m+1, r);
        merge(arr, l, m, r);
    }
}

void merge(ll arr[], ll l, ll m, ll r)
{
     // Your code here
    ll tempArr[r-l+1];
    ll a = l, b = m+1, c = 0;
    while(a <= m && b <= r) {
        if (arr[a] <= arr[b]) {
            tempArr[c] = arr[a];
            c++;
            a++;
        }
        else {
            tempArr[c] = arr[b];
            count = count +  (m - a + 1) ;
            c++;
            b++;
        }
    }
    while (a <= m) {
        tempArr[c] = arr[a];
        c++;
        a++;
    }
    while(b <= r) {
        tempArr[c] = arr[b];
        c++;
        b++;
    }
    ll u = 0;
    for (ll i = l; i <= r; i++) {
        arr[i] = tempArr[u];
        u++;
    }
}


int main() {
	ll t;
	cin>>t;
	while(t--){
	    ll n;
	    cin>>n;
	    ll arr[n];
	    for(ll i=0;i<n;i++){
	        cin>>arr[i];
	    }
	    mergeSort(arr,0,n-1);
	    cout<<count<<endl;
	    count = 0;
	}
	
	
	
	return 0;
}