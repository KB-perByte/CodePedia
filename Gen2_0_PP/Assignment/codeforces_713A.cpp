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
  



//-------------------------------------------------------------------

#include <cstdio>
typedef long long ll;
const int N = 262144;
int c[N];
int main() {
    int t, i, p; ll d; char op;
    scanf("%d", &t);
    while (t--) {
        for (op = getchar(); op == '\n'; op = getchar());
        scanf("%I64d", &d);
        for (i = p = 0; i < 18; ++i)
            p |= ((d % 10) & 1) << i, d /= 10;
        switch(op) {
        case '+': ++c[p]; break;
        case '-': --c[p]; break;
        case '?': printf("%d\n", c[p]); break;
        }
    }
    return 0;
}