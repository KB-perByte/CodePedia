#include <iostream>
#include<climits>
using namespace std;

int countSmallerEqualNumber(int arr[], int k, int N) {
	
	int c(0);
	for(int i = 0; i < N; i++) {
		if(arr[i] <= k) {
			c++;
		}
	}
	return c;
}

int main() {
	// your code goes here
	
	int arr[] = {7, 10, 4, 3, 20, 15}, k = 3;
	
	int minn = INT_MAX;
	int maxx = INT_MIN;
	for(int i = 0; i < 6; i++) {
		minn = min(minn, arr[i]);
		maxx = max(maxx, arr[i]);
	}
	
	int l = minn, h = maxx, mid, count1, count2;
	
	while(l <= h) {
		mid = (l+h) / 2;
		count1 = countSmallerEqualNumber(arr, mid, 6);
		
		if(count1 < k) {
			l = mid + 1;
		} else {
			count2 = countSmallerEqualNumber(arr, mid - 1, 6);
			
			if(count2 < k) {
				break;
			} else {
				h = mid -1;
			}
		}
	}
	
	cout<< mid <<endl;
}