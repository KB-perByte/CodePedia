include <bits/stdc++.h>

using namespace std;

long taumBday(int b, int w, int bc, int wc, int z) {
    if(bc==wc)
        return (long)(b+w)*(long)wc;
  
    else if(bc<wc && (bc+z) < wc)
        return ((long)(b+w)*(long)bc) +((long)w*(long)z);
    
    else if(wc<bc && (wc+z) < bc)
        return ((long)(b+w)*(long)wc) + ((long)b*(long)z);
    
    else 
        return ((long)b*(long)bc)+((long)w*(long)wc);   
}

int main()
{
    int t; cin>>t;
    while(t--)
    {
      int b,w,bc,wc,z;
      cin>>b>>w>>bc>>wc>>z;

      cout<<taumBday(b,w, bc, wc, z)<<endl;
    }
    return  0;
}# your code goes here