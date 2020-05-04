#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>
using namespace std;
char getK(int N, int d) 
{ 
    string _str; 
    stringstream ss; 
    ss << N; 
    ss >> _str; 
    return _str[d - 1]; 
} 

char processNth(int N) 
{ 
    long total = 0, nine = 9; 
    int dist = 0, len; 
    for (len = 1; ; len++) 
    { 
        total += nine*len; 
        dist += nine; 
        if (total >= N) 
        {
            total -= nine*len; 
            dist -= nine; 
            N -= total; 
            break; 
        } 
        nine *= 10; 
    } 
    int diff = ceil((double)N / len); 
    int d = N % len; 
    if (d == 0) 
        d = len; 
    return getK(dist + diff, d); 
}
    
int main() {

    int i= 0;
    int N= 0;
    cin>>i;
    for(int x=0; x<i; x++)
    {
        cin>>N;
        cout << processNth(N) << endl;
    }
    return 0;
}
