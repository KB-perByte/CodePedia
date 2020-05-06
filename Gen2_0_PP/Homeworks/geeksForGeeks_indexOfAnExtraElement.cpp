// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;
int findExtra(int a[], int b[], int n);
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int a[n], b[n - 1];
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        for (int i = 0; i < n - 1; i++) {
            cin >> b[i];
        }
        cout << findExtra(a, b, n) << endl;
    }
}// } Driver Code Ends


/*Complete the function below*/
int findExtra(int a[], int b[], int n) {
    // add code here.
    int start=0 ;
    int end=n-1 ;
    int index ;
   
    while(start<=end)
    {
        int mid=(start+end)/2 ;
       
        if(a[mid]==b[mid])
            start=mid+1 ;
           
        else
        {
            index=mid ;
            end=mid-1 ;
        }
    }
    return index ;

}