#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
#define ll long long
ll MOD= 1000000007;
vector<ll>primes;

bool sieveLst[1000007];

void precomSieve()
{
    ll i, j;
    for(i=2; i<1000004; i++) {
        if(!sieveLst[i])
        {
            primes.push_back(i);
            for(j=i+i; j<=1000004; j+=i)
                sieveLst[j]= 1;
        }
    }
}

int main() {
    ll l, r, q, ls, rs; 
    ll lhs, rhs, least, fact;
    vector<ll>::iterator L, R;
    memset(sieveLst, 0, sizeof sieveLst);
    precomSieve();
    cin>>q;
    while(q--)
    {
        cin>>l>>r;
        ls= round(sqrt(l));
        rs= round(sqrt(r));
        L= lower_bound(primes.begin(), primes.end(), ls);
        R= upper_bound(primes.begin(), primes.end(), rs);
        R--;
        least= *L;
        fact= *R;
        if(least*least < l) L++;
        if(fact*fact > r) R--;
        cout<<(R- L) +1<<endl;
    }
}