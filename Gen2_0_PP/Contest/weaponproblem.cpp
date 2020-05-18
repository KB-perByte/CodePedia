#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
typedef long long ll;

using namespace std;

bool ckeckDistribution(vector<ll> lst,int mid,int N,int K){
    ll sum=0;
    for(ll i=0;i<N;i++){
            sum+=lst[i]/mid;
    }
    return sum>=K;
}

ll distribution(vector<ll> lst,int N,int K){
    ll l=1;
    ll h=*max_element(lst.begin(),lst.end());
    while(l<=h){
        ll mid=l+(h-l)/2;
        bool check=ckeckDistribution(lst,mid,N,K);
        if(check){
                bool check2=ckeckDistribution(lst,mid+1,N,K);
                    if(!check2){
                        return mid;
                    }
                    else{
                    l=mid+1;
                    }
        }
        else{
            h=mid-1;
        }
    }
    return -1;
}

int main() {
ll N;
ll K;
ll a=0;
    cin>>N;
    cin>>K;
    vector<ll> lst;
    for(ll i=0;i<N;i++){
        cin>>a;
        lst.push_back(a);
    }
cout<<distribution(lst,N,K);
    return 0;
}