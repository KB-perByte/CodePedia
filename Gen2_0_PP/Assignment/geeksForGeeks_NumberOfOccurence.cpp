#include<bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--)
    {
        int n,x;
        cin>>n>>x;
        vector<int> a(n);
        for(int i=0;i<n;i++)
        {
            cin>>a[i];
        }
        int h=count(a.begin(),a.end(),x);
        if(h)
        cout<<h<<endl;
        else
        cout<<"-1"<<endl;
    }
         
	//code
	return 0;
}