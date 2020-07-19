#include <bits/stdc++.h>
#define ll __int64
using  namespace  std;
 
map<ll, int>mp;
 
ll change(ll a){
  ll res=0,t=1;
  while(a){
    res+=(a%10%2)*t;
    t*=10;
    a/=10;
  }
  return res;
}
 
int  main(){
  int t;
  while(~scanf("%d",&t)){
    mp.clear();
    char s[4];ll a;
    while(t--){
      scanf("%s%I64d",s,&a);
      ll tmp=change(a);
      if(s[0]=='+')mp[tmp]++;
      else if(s[0]=='-')mp[tmp]--;
      else printf("%d\n",mp[tmp]);
    }
  }
  return 0;
  