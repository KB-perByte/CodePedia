#include<bits/stdc++.h>
using namespace std;
int main()
{
	long int p,q,r;
	int n,i;
	cin>>n>>p>>q>>r;
	long long int a[n];
	for(i=0;i<n;++i)
	{
		cin>>a[i];
	}
	long long int maxpre[n];
	maxpre[0]=a[0]*p;
	for(i=1;i<n;++i)
	{
		maxpre[i]=max(a[i]*p,maxpre[i-1]);
	}
	long long int maxsuff[n];
	maxsuff[n-1]=a[n-1]*r;
	for(i=n-2;i>=0;i--)
	{
		maxsuff[i]=max(a[i]*r,maxsuff[i+1]);
	}
	long long int ans=LLONG_MIN;
	for(i=0;i<n;++i)
	{
		ans=max(ans,maxpre[i]+a[i]*q+maxsuff[i]);
	}
	cout<<ans;
	return 0;
}