#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<math.h>
#include<string.h>
#define LL long long
using namespace std;
long long int ans=1LL<<60;
char str[4];
void DFS_3(long long int a,long long int b)
{
    long long int temp=0;
    if(str[2]=='+')
        temp=a+b;
    else
        temp=a*b;
    ans=min(ans,temp);
}
void DFS_2(long long int a,long long int b,long long int c)
{
    if(str[1]=='+')
    {
        DFS_3(a+b,c);
        DFS_3(a+c,b);
        DFS_3(b+c,a);
    }
    else
    {
        DFS_3(a*b,c);
        DFS_3(a*c,b);
        DFS_3(b*c,a);
    }
}
void DFS_1(long long int a,long long int b,long long int c,long long int d)
{
    if(str[0]=='+')
    {
        DFS_2(a+b,c,d);
        DFS_2(a+c,b,d);
        DFS_2(a+d,b,c);
        DFS_2(b+c,a,d);
        DFS_2(b+d,a,c);
        DFS_2(c+d,a,b);
    }
    else
    {
        DFS_2(a*b,c,d);
        DFS_2(a*c,b,d);
        DFS_2(a*d,b,c);
        DFS_2(b*c,a,d);
        DFS_2(b*d,a,c);
        DFS_2(c*d,a,b);
    }
}
int main()
{
    long long int a,b,c,d;
    cin>>a>>b>>c>>d;
    cin>>str[0]>>str[1]>>str[2];
    DFS_1(a,b,c,d);
    cout<<ans<<endl;
}
