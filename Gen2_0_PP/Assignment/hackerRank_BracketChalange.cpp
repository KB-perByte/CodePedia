#include <cmath>
#include <cstdio>
#include<bits/stdc++.h>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#define ll long long int

void helper(ll l1, ll r1, ll l2, ll r2, ll N, ll M, string str) {
    
    if (l1 + r1 + l2 + r2 == 2*(M+N)) {
        cout << str << "\n";
        str.clear();
        return;
    }
    
    if (l1 < N) {
        str += '(';
        helper(l1+1,r1,l2,r2,N,M,str);
        str.pop_back();
    }
    if (l2 < M) {
        str += '{';
        helper(l1,r1,l2+1,r2,N,M,str);
        str.pop_back();
    }
    ll c1 = 0, c2 = 0;
    for (ll j = str.size()-1; j >= 0; j--) {
        if (str[j] == '}')
            c2++;
        else if (str[j] == ')')
            c1++;
        else if (str[j] == '{')
            c2--;
        else if (str[j] == '(')
            c1--;
        if (c1 < 0 || c2 < 0)
            break;
    }
    
    if (c1 < 0) {
        str += ')';
        helper(l1,r1+1,l2,r2,N,M,str);
        str.pop_back();
    }
    if (c2 < 0){
        str += '}';
        helper(l1,r1,l2,r2+1,N,M,str);
        str.pop_back();
    }
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    ll N, M;
    cin >> N >> M;
    helper(0,0,0,0,N,M,"");
    return 0;
}
