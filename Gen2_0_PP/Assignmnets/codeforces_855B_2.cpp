#include<bits/stdc++.h>
using namespace std;
long long int Answer(vector<long long int> & A,long long int N,long long int P,long long int Q,long long int R)
{
    vector<long long int>Suf(N);
    Suf[N-1] = R*A[N-1];
    for(int i=N-2;i>=0;i--)
        Suf[i] = max(Suf[i+1],R*A[i]);
    long long int ans = LLONG_MIN;
    long long int Pre = A[0]*P;
 
    for(int j=0;j<N;j++)
    {
        Pre = max(Pre,(A[j]*P));
        ans = max(ans,(Pre + Q*A[j] + Suf[j]));
       
    }
    return ans;
}
int main()
{
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    long long int N,P,Q,R;
    cin>>N>>P>>Q>>R;
    vector<long long int>A(N);
    for(int i=0;i<N;i++)
        cin>>A[i];
    
    cout<<Answer(A,N,P,Q,R);
}