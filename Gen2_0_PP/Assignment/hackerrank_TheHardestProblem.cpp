#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#define ll long long int
ll arr[100001];

ll findGCD (ll A, ll B) {
    if (A == 0)
        return B;
    return findGCD(B%A, A);
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    ll T;
    
    cin >> T;
    
    while(T--) {
        ll N;
        
        cin >> N;
        
        for (ll i = 0; i < N; i++) {
             cin >> arr[i];
        }
        
        ll A = arr[0];
        for (ll i = 1; i < N; i++) {
            A = findGCD(arr[i],A);
            if (A == 1){
                break;
            }
        }
        
        if (A == 1)
            cout << "1" << endl;
        else
            cout << "0" << endl;
        
    }
    return 0;
}