#include<bits/stdc++.h>
using namespace std;
#define fast ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define int long long
void postorder(vector<int> &a,int n,int l,int r,int &i,int &k)
{
    if(l>r || i==n || a[i]<l || a[i] > r)
    return;
    int val=a[i++];
    postorder(a,n,l,val-1,i,k);
    postorder(a,n,val+1,r,i,k);
    a[k++]=val;
}
signed main()
 {
	fast
	int t,n;
	cin>>t;
	while(t--)
	{
	    cin>>n;
	    vector<int> a(n);
	    for(int i=0;i<n;i++)
	    cin>>a[i];
	    int ind=0,ind1=0;
	    postorder(a,n,INT_MIN,INT_MAX,ind,ind1);
	    for(auto i:a)
	    cout<<i<<" ";cout<<endl;
	}
	return 0;
}