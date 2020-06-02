#include <bits/stdc++.h>
using namespace std;


bool isPossible23(vector<int> &arr, int result, int j){
	if(result == 23 && j == arr.size()){
		return true;
	}

	for(int i = 0; i < arr.size(); i++){
		if(result == INT_MIN){
			int temp = arr[i];
			arr[i] = -1;
			bool ans = isPossible23(arr, temp, j + 1);
			arr[i] = temp;
			if(ans){
				return true;
			}
		}
		else{
			if(arr[i] != -1){
				int temp = arr[i];
				arr[i] = -1;
				bool ans = isPossible23(arr, result + temp, j + 1) || isPossible23(arr, result*temp, j + 1) || isPossible23(arr, result - temp, j + 1);
				arr[i] = temp;
				if(ans){
					return true;
				}
			}
		}
	}
	return false;
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	while(true){
		vector<int> arr(5);
		for(int i = 0; i < 5; i++){
			cin>>arr[i];
		}
		if(arr[0] == 0){
			break;
		}
		if(isPossible23(arr, INT_MIN, 0)){
			cout<<"Possible"<<endl;
		}
		else{
			cout<<"Impossible"<<endl;
		}
	}
}
