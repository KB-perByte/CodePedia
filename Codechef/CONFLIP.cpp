#include <iostream>
using namespace std;

int main() {
    int T; cin>>T;
    while(T--)
    {
          int G; cin>>G;
          while(G--)
          {
              int I,N,Q;
              cin>>I>>N>>Q;
              int count = N / 2;

              if ((I == 1 && Q == 1) || (I == 2 && Q == 2))
                    count = count;
              else if ((I == 1 && Q == 2) || (I == 2 && Q == 1))
                    count = N - count;
              cout<<count<<endl;
          }
	   }return 0;
}