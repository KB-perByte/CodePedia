#include <bits/stdc++.h>
using namespace std;

int main() {
	int T;
	cin>>T;
	while(T--){
	    int N;
	    cin>>N;
	    vector<pair<int,int>> arr(N);
	    for(int i = 0; i < N; i++){
	        int a;
	        cin>>a;
	        arr[i] = make_pair(a, i);
	    }
	    sort(arr.begin(), arr.end());
	    int ans = 0;
	    int minTillNow = arr[0].second;
	    for(int i = 1; i < N; i++){
	        ans = max(ans, arr[i].second - minTillNow);
	        minTillNow = min(minTillNow, arr[i].second);
	    }
	    cout<<ans<<endl;
	}
	return 0;
}