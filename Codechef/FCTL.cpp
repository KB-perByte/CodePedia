#include <iostream>
using namespace std;

int main(void) 
{
    int T; 
    cin>>T;
    while(T--)
    {
        int zero=0, N;
        cin>>N;
        while(N>4)
        {
           N = N/5;
           zero +=N;
        }
        cout<<zero<<endl;
    }
    return 0;
}