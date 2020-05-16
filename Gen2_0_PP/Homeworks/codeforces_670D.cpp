#include<bits/stdc++.h>
using namespace std;
const int maxn = 1e5+7;
long long a[maxn],b[maxn],k;
int n;
bool check(long long x)
{
    long long ans = 0;
    for(int i=1;i<=n;i++)
        if(a[i]*x-b[i]>k)return false;
    for(int i=1;i<=n;i++)
        ans+=max(a[i]*x-b[i],0LL);
    if(ans<=k)return true;
    return false;
}
int main()
{
    scanf("%d%lld",&n,&k);
    for(int i=1;i<=n;i++)scanf("%lld",&a[i]);
    for(int i=1;i<=n;i++)scanf("%lld",&b[i]);
    long long l=0,r=2e9,ans=0;
    while(l<=r)
    {
        int mid=(l+r)/2;
        if(check(mid))l=mid+1,ans=mid;
        else r=mid-1;
    }
    cout<<ans<<endl;
}