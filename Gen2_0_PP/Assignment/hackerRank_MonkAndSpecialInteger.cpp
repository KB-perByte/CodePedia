#include<bits/stdc++.h>
using namespace std;
typedef long long int llint;
bool checkFnc(vector<llint> a,llint k,llint x){
	llint s = 0;
	for(llint i = 0; i < k; i++) s += a[i];

	if(s > x) return false;
	llint j = 0;
	for(llint i = k; i < a.size(); i++){
		s += a[i];
		s -= a[j];
		if(s > x) return false;

		j++;
	}
	return true;

}

int main(){

	llint n,x;
	cin >> n >> x;
	vector<llint> a(n);

	for(llint i = 0; i < n; i++) cin >> a[i];

	llint l = 1, r = n;
	llint ele;
	while(l <= r){
		llint mid = (l + r) / 2;

		if(checkFnc(a,mid,x)){
			if(!checkFnc(a,mid+1,x)){
				ele = mid;
				break;
			}
			else l = mid + 1;
		}
		else{
			r = mid - 1;
		}
	}
	cout << ele <<"\n";
}