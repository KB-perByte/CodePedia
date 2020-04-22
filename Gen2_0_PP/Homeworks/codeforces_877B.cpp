#include<stdio.h>
#include<string>
#include<iostream>
using namespace std;
int main()
{
    string s;
    while(cin>>s)
    {
        int a=0,ab=0,aba=0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='a')
            {
                a++;aba++;
            }
            if(s[i]=='b')
                ab++;
            aba=max(aba,ab);
            ab=max(ab,a);
        }
        cout<<aba<<endl;
    }
}

