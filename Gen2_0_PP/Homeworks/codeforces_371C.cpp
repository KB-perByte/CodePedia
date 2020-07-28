#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
 
using namespace std;
 
int main()
{
    long long int B=0,S=0,C=0,r,nb,ns,nc,pb,ps,pc,ans=0;
    string s;
    cin>>s;
    for(int i=0;i<s.size();i++)
    {
        if(s[i]=='B') B++;
        if(s[i]=='C') C++;
        if(s[i]=='S') S++;
    }
    int tx=0,t1=0;
    tx=(B>0)+(C>0)+(S>0);
    cin>>nb>>ns>>nc>>pb>>ps>>pc>>r;
    int prise=B*pb+C*pc+S*ps;
    bool flag=true;
    while(r>0)
    {
        if((nb||nc||ns)&&flag)
        {
            bool flagB=false,flagC=false,flagS=false;
            if(nb>=B) nb-=B,flagB=true;
            else
            {
                int buy=B-nb; nb=0;
                if(r>=buy*pb) r-=buy*pb,flagB=true;
                else break;
            }
 
            if(nc>=C) nc-=C,flagC=true;
            else
            {
                int buy=C-nc; nc=0;
                if(r>=buy*pc) r-=buy*pc,flagC=true;
                else break;
            }
 
            if(ns>=S) ns-=S,flagS=true;
            else
            {
                int buy=S-ns; ns=0;
                if(r>=buy*ps) r-=buy*ps,flagS=true;
                else break;
            }
            t1=(nb==0)+(nc==0)+(ns==0);
            if(t1==tx) flag=false;
            if(flagB&&flagC&&flagS) ans++;
            else break;
        }
        else
        {
            ans+=r/prise;
            break;
        }
    }
    cout<<ans<<endl;
    return 0;
}


