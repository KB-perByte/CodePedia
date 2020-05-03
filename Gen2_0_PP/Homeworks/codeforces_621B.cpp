#include <cstdio>
#include <iostream>
using namespace std;

int a[3000];
int b[3000];
int x , y;
long long sum;

main()
{
    int n;
    cin >> n;
    for(int i = 0; i < n; i ++)
   {
        cin >> x >> y;
        sum += a[x+y]++;
        sum += b[1000+x-y]++;
    }
   cout<<sum;
}