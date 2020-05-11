#include <iostream>
using namespace std;

int main() {
	int n;
	cin>>n;
	int arr[n],i;
	for(i=0;i<n;i++)
	{
		cin>>arr[i];
	}
	int l=0,h=n-1;
	while(l<=h)
	{
		int m=(l+h)/2;
		if(arr[m]==m&&arr[m-1]==arr[m])
		{
			cout<<arr[m];
			break;
		}
		else if(arr[m]>m)
		{
			l=m+1;
		}
		else if(arr[m]==m)
		{
			h=m-1;
		}
	}
	
	return 0;
}