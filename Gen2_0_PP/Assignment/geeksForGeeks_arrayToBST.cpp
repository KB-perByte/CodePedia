#include <iostream>
using namespace std;

void printpreorder(int *arr,int low,int high){
    if(low>high)return;
    int mid=(low+((high-low)/2));
    cout<<arr[mid]<<" ";
    printpreorder(arr,low,mid-1);
    printpreorder(arr,mid+1,high);
}
int main() {
	int tc;
	cin>>tc;
	while(tc--){
	    int size;
	    cin>>size;
	    int *arr=new int[size];
	    for(int i=0;i<size;i++)
	        cin>>arr[i];
	  printpreorder(arr,0,size-1);
	  cout<<endl;
	}
	return 0;
}