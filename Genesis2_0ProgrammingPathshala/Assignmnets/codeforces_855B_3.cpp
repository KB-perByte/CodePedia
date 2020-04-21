#include<bits/stdc++.h>
#define ll long long int
#define mod 1000000007
#define all(v) v.begin(),v.end()
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    ll n,p,q,r;
    cin>>n>>p>>q>>r;
    vector<ll> a(n);
    vector<pair<ll,ll> > pa;
    for(ll i=0;i<n;i++)
    {
        cin>>a[i];
    }
    ll dp[4][n];
    dp[1][0] = p*a[0];
    dp[2][0] = q*a[0] + dp[1][0];
    dp[3][0] = r*a[0] + dp[2][0];
    for(int i=1;i<n;i++)
    {
        dp[1][i] = max(dp[1][i-1],p*a[i]);
    }
    for(int i=1;i<n;i++)
    {
        dp[2][i] = max(dp[2][i-1],q*a[i]+dp[1][i]);
    }
    for(int i=1;i<n;i++)
    {
        dp[3][i] = max(dp[3][i-1],r*a[i]+dp[2][i]);
    }
    cout<<dp[3][n-1];
    return 0;
}