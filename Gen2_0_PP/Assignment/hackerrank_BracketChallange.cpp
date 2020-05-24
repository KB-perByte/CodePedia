#include<bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define ll long long
#define rep(i,a,b) for(ll i=a;i<b;i++)
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define ios ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)

vector<ll> fact(10,1); 
ll gcd(ll n1,ll n2){
    ll maxm=max(n1,n2);
    ll minm=min(n1,n2);
    if((maxm%minm)==0) return minm;
    else return gcd(minm,maxm%minm);
}
 
ll power(ll x, ll y) 
{ 
    ll temp; 
    if( y == 0) 
        return 1; 
    temp = power(x, y/2)%mod; 
    if (y%2 == 0) 
        return temp*temp%mod; 
    else
        return (x*temp%mod)*temp%mod; 
}
ll ifact(long long k){
    return power(fact[k],mod-2)%mod;
}
ll ncr(ll n, ll r){
    if(n<r) return 0;
    ll num=1;
    ll den=1;
    ll g;
    rep(i,1,r+1){
        num=num*(n-i+1);
        den=den*(i);
        g=gcd(num,den);
        num=num/g;
        den=den/g;
    }
    return num;
}
int n,m;
void PPBP(char str[],int N,int ind,int l1, int r1, int l2, int r2){
    if(ind==N){
        for(int i=0;i<N;i++) cout<<str[i];
        cout<<endl;
        return;
    }
    if(l1<n){
        str[ind]='(';
        PPBP(str,N,ind+1,l1+1,r1,l2,r2);
    }
    if(l2<m){
        str[ind]='{';
        PPBP(str,N,ind+1,l1,r1,l2+1,r2);
    }
    if(l1>r1){
        int i,c=0;
        for(i=ind-1;i>=0;i--){
            if(str[i]=='{' || str[i]=='(') c++;
            if(c==1) break;
            if(str[i]=='}' || str[i]==')') c--;
        }
         if(c>0 && str[i]=='('){
            str[ind]=')';
            PPBP(str,N,ind+1,l1,r1+1,l2,r2);
        }

    }
    if(l2>r2){
        int i,c=0;
        for(i=ind-1;i>=0;i--){
            if(str[i]=='{' || str[i]=='(') c++;
            if(c==1) break;
            if(str[i]=='}' || str[i]==')') c--;
        }
         if(c>0 && str[i]=='{'){
            str[ind]='}';
            PPBP(str,N,ind+1,l1,r1,l2,r2+1);
        }
    }
}

int main(){
   ios;
   int t=1;//cin>>t;
   while(t--){
       cin>>n>>m;
       int N=2*(n+m);
       char str[N];
       PPBP(str,N,0,0,0,0,0);
    } 
}
