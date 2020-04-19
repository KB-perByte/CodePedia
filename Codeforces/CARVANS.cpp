#include <bits/stdc++.h>
using namespace std;

int main() {
    int T, N,s; 
    cin>>T;
    while(T--)
    {
        cin>>N;
        int max= INT_MAX ,count=0;
        for(int i=0;i<N;i++)
        {
            cin>>s;
            if(s<=max)
            {
                count++;
                max=s;
            }
        }
        cout<<count<<endl;
    }
    return 0;
}