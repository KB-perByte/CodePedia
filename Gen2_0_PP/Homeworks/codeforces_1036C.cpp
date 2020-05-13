#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
using namespace std;
typedef long long ll;
ll dp[40][4];
ll a[40];

ll dfs(int pos,int pre,int sta,bool limit)
{
    if(sta>=4) return 0;
    if(pos==-1) return 1;  
    if(!limit&&dp[pos][sta]!=-1) return dp[pos][sta];
    int up=limit ? a[pos] : 9;
    ll tmp=0;
    for(int i=0;i<=up;i++)
    {
    	int nsta=sta;
        if(i!=0) nsta++;
        tmp+=dfs(pos-1,i,nsta,limit&&i==up);
    }
    if(!limit) dp[pos][sta]=tmp;
    return tmp;
}
ll solve(ll x)
{
    int pos=0;
    while(x)
    {
        a[pos++]=x%10;
        x/=10;
    }
    return dfs(pos-1,-1,0,1);
}
int main()
{
    ll le,ri; 
	int t;
	scanf("%d",&t);      
    while(t--){
    	scanf("%lld%lld",&le,&ri);
    	memset(dp,-1,sizeof dp); 
        printf("%lld\n",solve(ri)-solve(le-1));
	}
}